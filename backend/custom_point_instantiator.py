from .custom_exceptions import PointNotFound, EvaluationError
from .db import engine, PointValue, CustomPointDefinition
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()


def find_required_points_value(dev_id: str, point_type: str) -> float:
    """Retrieves a single point value"""

    latest_point_value = (
        session.query(PointValue)
        .where(dev_id == dev_id)
        .where(point_type == point_type)
        .first()
    )

    if latest_point_value:
        return latest_point_value.value

    message = "{} is required but not found in the latest_point histories".format(
        point_type
    )
    raise PointNotFound(message)


def get_first_argument(custom_point_definition: dict) -> float:
    """Returns value to left of operand"""
    dev_id = custom_point_definition.get("dev_id", None)

    dependent_point_type = custom_point_definition.get("dependent_point_type", None)

    return find_required_points_value(dev_id, dependent_point_type)


def get_second_argument(custom_point_definition: dict) -> float:
    """Returns value to right of operand"""
    dev_id = custom_point_definition.get("dev_id", None)

    variable_value = custom_point_definition.get("variable_value", None)

    if variable_value:
        argument = find_required_points_value(dev_id, variable_value)
    else:
        argument = custom_point_definition.get("raw_value", None)

    return argument


def get_custom_point_value(custom_point_definition: dict) -> float:
    """Instantiates custom point value"""

    first_arg = get_first_argument(custom_point_definition)

    second_arg = get_second_argument(custom_point_definition)

    operator = custom_point_definition.get("operator", None)

    try:
        equation = "{} {} {}".format(first_arg, operator, second_arg)
        return int(eval(equation))
    except Exception as e:
        message = "There was an error processing value: {}".format(e)
        raise EvaluationError(message)


def instantiate_values() -> None:
    custom_points = session.query(CustomPointDefinition).all()

    custom_point_values = []

    for custom_point in custom_points:
        custom_point_dict = custom_point.__dict__
        custom_point_value = get_custom_point_value(custom_point_dict)

        custom_point_values.append(
            PointValue(
                dev_id=custom_point.dev_id,
                point_type=custom_point.point_type,
                units=custom_point.units,
                value=custom_point_value,
            )
        )

    session.add_all(custom_point_values)
    session.commit()
