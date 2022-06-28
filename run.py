from computed_point_instantiator.app import handler

event = {
    "messages": [
        {
            "original_measure": {
                "dev_id": "dev1",
                "device_type": "sensor1",
                "point_type": "temp",
                "tmst": "2021-11-03 15:01:45.833454",
                "topic": "measure",
                "units": "celsius",
                "value": 10,
            },
            "computed_definition": {
                "dev_id": "dev1",
                "point_type": "high_temp",
                "units": "bool",
                "dependent_point_type": "temp",
                "operator": ">=",
                "raw_value": 15,
                "variable_value": None,
            },
        },
        {
            "original_measure": {
                "dev_id": "dev2",
                "device_type": "sensor2",
                "point_type": "load",
                "tmst": "2021-11-03 15:01:45.833454",
                "topic": "measure",
                "units": "kwh",
                "value": 50,
            },
            "computed_definition": {
                "dev_id": "dev2",
                "point_type": "load_greater_than_power",
                "units": "bool",
                "dependent_point_type": "load",
                "operator": ">",
                "raw_value": None,
                "variable_value": "power",
            },
        },
    ]
}

if __name__ == "__main__":
    handler(event)
