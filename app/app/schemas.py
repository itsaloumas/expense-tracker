from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel
from datetime import datetime
class ExpenseCreate(BaseModel):
    description: str
    amount: float
    category: str

class ExpenseUpdate(BaseModel):
    description: str | None = None
    amount: float | None = None
    category: str | None = None

class Expense(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    date: datetime  # ή date: datetime | None
    class Config:
        orm_mode = True