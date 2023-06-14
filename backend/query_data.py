from .db import PointValue, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import and_


session = sessionmaker(bind=engine)()


def most_recent_points():
    # Query for the most recent record for each point_type
    subquery = (
        session.query(
            PointValue.point_type,
            PointValue.dev_id,
            func.max(PointValue.time).label("max_time"),
        )
        .group_by(PointValue.point_type, PointValue.dev_id)
        .subquery()
    )

    query = (
        session.query(PointValue)
        .join(
            subquery,
            and_(
                PointValue.dev_id == subquery.c.dev_id,
                PointValue.point_type == subquery.c.point_type,
                PointValue.time == subquery.c.max_time,
            ),
        )
        .order_by(PointValue.dev_id)
    )

    # Execute the query and retrieve the results
    results = query.all()

    result_dicts = [
        {
            "id": record.id,
            "dev_id": record.dev_id,
            "point_type": record.point_type,
            "units": record.units,
            "value": record.value,
            "time": record.time,
        }
        for record in results
    ]

    return result_dicts
