from numbers import Number
from data.points import return_sample_data
from .get_custom_point_value import get_custom_point_value
from .custom_exceptions import PointsNotFound
from copy import deepcopy


# this would usually be a db call
def get_latest_points(dev_id: str) -> list[dict]:
    """Retrieves points for a given device"""

    try:
        return return_sample_data(dev_id)
    except PointsNotFound as e:
        message = "The following error occured while returning points: {}".format(e)
        raise PointsNotFound(message)


def construct_pipeline_message(original_message: dict) -> dict:
    """Constructs New custom Point Messages"""

    original_measure = original_message["original_measure"]
    dev_id = original_measure["dev_id"]

    latest_points = get_latest_points(dev_id)

    custom_point_definition = original_message["custom_point_definition"]

    custom_value = get_custom_point_value(latest_points, custom_point_definition)

    new_message = deepcopy(original_measure)
    new_message["value"] = custom_value
    new_message["point_type"] = custom_point_definition["point_type"]
    new_message["units"] = custom_point_definition["units"]

    return new_message


def publish_pipeline_messages(new_messages: dict) -> None:
    """Passes custom Points Messages to Pipeline for Processing"""

    print(new_messages)
    for message in new_messages:
        print(
            "A new point value was calculated for {} with a value of {}".format(
                message["point_type"], message["value"]
            )
        )


def handler(event: dict) -> None:
    """Orchestrates custom point instantiation functionality"""

    messages = event["messages"]

    new_messages = [construct_pipeline_message(message) for message in messages]

    if new_messages:
        publish_pipeline_messages(new_messages)
    else:
        print("No new messages to send in pipeline from {}".format(event))
