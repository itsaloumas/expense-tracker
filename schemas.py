from pydantic import BaseModel
from datetime import datetime

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    category: str

class Expense(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    date: datetime

    class Config:
        orm_mode = True