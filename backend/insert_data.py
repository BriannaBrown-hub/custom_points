from sqlalchemy import insert
import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db.engine)
session = Session()


sample_data = [
    {"dev_id": "dev1", "point_type": "temp", "units": "celsius", "value": 10},
    {"dev_id": "dev1", "point_type": "power", "units": "kwh", "value": 50},
    {"dev_id": "dev2", "point_type": "temp", "units": "celsius", "value": 35},
    {"dev_id": "dev2", "point_type": "load", "units": "kwh", "value": 50},
    {"dev_id": "dev2", "point_type": "power", "units": "kwh", "value": 40},
]

for data in sample_data:
    session.execute(insert(db.LatestPointValue), data)

session.commit()
