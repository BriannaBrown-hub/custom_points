sample_data = [
    {
        "dev_id": "dev1",
        "points": [
            {"point_type": "temp", "units": "celsius", "value": 10},
            {"point_type": "power", "units": "kwh", "value": 50},
        ],
    },
    {
        "dev_id": "dev2",
        "points": [
            {"point_type": "temp", "units": "celsius", "value": 35},
            {"point_type": "load", "units": "kwh", "value": 50},
            {"point_type": "power", "units": "kwh", "value": 40},
        ],
    },
]


def return_sample_data(dev_id):
    return next(
        (data["points"] for data in sample_data if data["dev_id"] == dev_id),
        None,
    )
