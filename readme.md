# Custom Points Instantiator

## About

This is a (modified) portion of a solution that allows for platform users to develop custom points based off of existing sensor data. This is a useful feature to customers as it allows for customization and value to the platform.

As data is read from sensors, a listener checks for custom point dependencies. If a dependency is found, the original data message, along with the custom point definition is routed to this solution.

After the custom point value is determined, the message would be returned to the data pipeline for further analysis and storage.

## Custom Points

Custom points have the following definition:

```
{
  "dev_id": string,
  "point_type": string,
  "units": string,
  "dependent_point_type": string,
  "operator": string(+, -, /, *, ==, >=, <=, >, <),
  "raw_value": float,
  "variable_value": string,
}
```

The `dependent_point_type` is used to lookup the latest value stored (usually stored in the database).

A custom point must have either a `raw_value` or `variable_value`. If a `variable_value` is specified, this too will be looked up in the latest value store.

The `dependent_point_value`, `operator` and `raw_value` or `variable_value` are used to evaluate the `custom_point` value.

## Environment

This solution has been modified to run locally. In production, this solution exists as a lambda that is triggered by an SQS queue and interacts with a postgreSQL database.

## Running the simulation

To run this program enter the following in the command line:

```
python run.py
```

To simulate an error an `-error` flag can be added.
