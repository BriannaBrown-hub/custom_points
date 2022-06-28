from numbers import Number
from data.points import return_sample_data
from .get_computed_point_value import get_computed_point_value
from .custom_exceptions import PointsNotFound
from copy import deepcopy


# this would usually be a db call
def get_latest_points(dev_id: str) -> list[dict]:
    try:
        return return_sample_data(dev_id)
    except PointsNotFound as e:
        message = "The following error occured while returning points: {}".format(e)
        raise PointsNotFound(message)


def construct_pipeline_message(original_message: dict) -> dict:
    original_measure = original_message["original_measure"]
    dev_id = original_measure["dev_id"]

    latest_points = get_latest_points(dev_id)

    computed_point_definition = original_message["computed_definition"]

    computed_value = get_computed_point_value(latest_points, computed_point_definition)

    new_message = deepcopy(original_measure)
    new_message["value"] = computed_value
    new_message["point_type"] = computed_point_definition["point_type"]
    new_message["units"] = computed_point_definition["units"]

    return new_message


def publish_pipeline_messages(new_messages: dict) -> None:
    print(new_messages)
    for message in new_messages:
        print(
            "A new point was constructed for {} with a value of {}".format(
                message["point_type"], message["value"]
            )
        )


def handler(event: dict) -> None:
    messages = event["messages"]

    new_messages = [construct_pipeline_message(message) for message in messages]

    if new_messages:
        publish_pipeline_messages(new_messages)
    else:
        print("No new messages to send in pipeline from {}".format(event))
