from sqlalchemy import Column, Integer, String, String, Float, DateTime
from datetime import datetime
from .database import Base
from zoneinfo import ZoneInfo

class Expense(Base):
    __tablename__="expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable =False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable = False)
    date = Column(DateTime, default = datetime.now(ZoneInfo("Europe/Athens")))
