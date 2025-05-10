# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(255), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)