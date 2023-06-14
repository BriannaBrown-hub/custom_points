from flask import Flask, request
from .query_data import most_recent_points
from .db import engine, CustomPointDefinition, PointValue
from flask_cors import CORS
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker
from .custom_point_instantiator import instantiate_values

session = sessionmaker(bind=engine)()

app = Flask(__name__)
CORS(app)


@app.route("/delete_data", methods=["DELETE"])
def delete_data():
    session.query(CustomPointDefinition).delete()
    session.query(PointValue).delete()
    session.commit()
    return "Data deleted successfully", 200


@app.route("/seed_data", methods=["POST"])
def seed_data():
    sample_data = [
        {"dev_id": "dev1", "point_type": "temp", "units": "celsius", "value": 10},
        {"dev_id": "dev1", "point_type": "power", "units": "kwh", "value": 50},
        {"dev_id": "dev2", "point_type": "temp", "units": "celsius", "value": 35},
        {"dev_id": "dev2", "point_type": "load", "units": "kwh", "value": 50},
        {"dev_id": "dev2", "point_type": "power", "units": "kwh", "value": 40},
    ]

    for data in sample_data:
        session.execute(insert(PointValue), data)

    session.commit()

    return "Data seeded successfully", 200


@app.route("/get_latest_points")
def query_latest_points():
    return most_recent_points()


@app.route("/create_custom_point", methods=["POST"])
def create_custom_point():
    data = request.json
    custom_point = CustomPointDefinition(
        dev_id=data["dev_id"],
        point_type=data["point_type"],
        units=data["units"],
        dependent_point_type=data["dependent_point_type"],
        operator=data["operator"],
        raw_value=data["raw_value"],
        variable_value=data["variable_value"],
    )
    session.add(custom_point)
    session.commit()
    return "Custom Point created successfully", 200


@app.route("/calculate_custom_point_values")
def calculate_custom_point_value():
    instantiate_values()

    return "Custom Point values calculated successfully", 200


if __name__ == "__main__":
    app.run(debug=True)
