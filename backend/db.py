from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine("sqlite:///database.db", echo=True)

Base = declarative_base()


class PointValue(Base):
    __tablename__ = "point_values"

    id = Column(Integer, primary_key=True)
    dev_id = Column(String)
    custom_point = Column(Boolean)
    point_type = Column(String)
    units = Column(String)
    value = Column(Float)
    time = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return (
            "<Point Value(dev_id='%s', custom_point='%s', point_type='%s', units='%s', value='%s', time='%s')>"
            % (
                self.dev_id,
                self.custom_point,
                self.point_type,
                self.units,
                self.value,
                self.time,
            )
        )


class CustomPointDefinition(Base):
    __tablename__ = "custom_point_definitions"

    id = Column(Integer, primary_key=True)
    dev_id = Column(String)
    point_type = Column(String)
    units = Column(String)
    dependent_point_type = Column(String)
    operator = Column(String)
    raw_value = Column(String)
    variable_value = Column(String)

    def __repr__(self):
        return (
            "<Custom Point Definition(dev_id='%s', point_type='%s', units='%s', dependent_point_type='%s', operator='%s', raw_value='%s', variable_value='%s')>"
            % (
                self.dev_id,
                self.point_type,
                self.units,
                self.dependent_point_type,
                self.operator,
                self.raw_value,
                self.variable_value,
            )
        )


Base.metadata.create_all(engine)
