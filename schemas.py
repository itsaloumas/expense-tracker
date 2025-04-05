from pydantic import BaseModel
from datetime import datetime


class Expense(BaseModel):
    id: int | None = None
    description: str
    amount: float
    category: str
    date: datetime | None=None

    class Config:
        orm_mode = True