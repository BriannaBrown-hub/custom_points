from .custom_exceptions import PointNotFound, EvaluationError


def find_required_points_value(latest_points: list[dict], required_point: str) -> float:
    """Retrieves a single point value"""

    value = next(
        (
            point["value"]
            for point in latest_points
            if point["point_type"] == required_point
        ),
        None,
    )

    if value:
        return value

    message = "{} is required but not found in the latest_point histories".format(
        required_point
    )
    raise PointNotFound(message)


def get_first_argument(
    latest_points: list[dict], custom_point_definition: dict
) -> float:
    """Returns value to left of operand"""

    dependent_point_type = custom_point_definition.get("dependent_point_type", None)

    return find_required_points_value(latest_points, dependent_point_type)


def get_second_argument(
    latest_points: list[dict], custom_point_definition: dict
) -> float:
    """Returns value to right of operand"""

    variable_value = custom_point_definition.get("variable_value", None)

    if variable_value:
        argument = find_required_points_value(latest_points, variable_value)
    else:
        argument = custom_point_definition.get("raw_value", None)

    return argument


def get_custom_point_value(
    latest_points: list[dict], custom_point_definition: dict
) -> float:
    """Instantiates custom point value"""

    first_arg = get_first_argument(latest_points, custom_point_definition)

    second_arg = get_second_argument(latest_points, custom_point_definition)

    operator = custom_point_definition.get("operator", None)

    try:
        equation = "{} {} {}".format(first_arg, operator, second_arg)
        return int(eval(equation))
    except Exception as e:
        message = "There was an error processing value: {}".format(e)
        raise EvaluationError(message)
