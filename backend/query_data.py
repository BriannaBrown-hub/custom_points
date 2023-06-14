from .db import LatestPointValue, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import and_


session = sessionmaker(bind=engine)()


def most_recent_points():
    # Query for the most recent record for each point_type
    subquery = (
        session.query(
            LatestPointValue.point_type,
            LatestPointValue.dev_id,
            func.max(LatestPointValue.time).label("max_time"),
        )
        .group_by(LatestPointValue.point_type, LatestPointValue.dev_id)
        .subquery()
    )

    query = session.query(LatestPointValue).join(
        subquery,
        and_(
            LatestPointValue.dev_id == subquery.c.dev_id,
            LatestPointValue.point_type == subquery.c.point_type,
            LatestPointValue.time == subquery.c.max_time,
        ),
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
