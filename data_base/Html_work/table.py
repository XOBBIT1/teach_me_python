import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    String
)

Base = declarative_base()

class Info(Base):
    __tablename__ = "info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_product = Column(Text(100), unique=True)
    day_time = Column(DateTime, default=datetime.datetime.utcnow())
    url = Column(String, unique=True, nullable=False)