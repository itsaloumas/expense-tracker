from fastapi import FastAPI, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from .database import engine, SessionLocal
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response   # 👈 για το /metrics

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

REQUEST_COUNTER = Counter(
    "expense_api_requests_total",
    "Total HTTP requests to Expense Tracker API"
)

@app.middleware("http")
async def count_requests(request: Request, call_next):
    REQUEST_COUNTER.inc()
    return await call_next(request)

@app.get("/metrics")
def metrics():
    """Expose Prometheus metrics."""
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/expenses", response_model=list[schemas.Expense])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()

@app.get("/expenses/total", status_code=200)
def get_total_expenses(db: Session = Depends(get_db)):
    total = db.query(func.sum(models.Expense.amount)).scalar() or 0
    return {"total_amount": total}

@app.get("/expenses/{expense_id}", response_model=schemas.Expense)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Expense with id {expense_id} not found")
    return expense

@app.get("/expenses/by_category/total", status_code=200)
def get_total_by_category(category: str, db: Session = Depends(get_db)):
    total = (db.query(func.sum(models.Expense.amount))
               .filter(models.Expense.category == category)
               .scalar() or 0)
    return {"category": category, "total_amount": total}

@app.post("/expenses", response_model=schemas.Expense,
          status_code=status.HTTP_201_CREATED)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.put("/expenses/{expense_id}", response_model=schemas.Expense)
def update_expense(expense_id: int, expense_update: schemas.ExpenseUpdate,
                   db: Session = Depends(get_db)):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Expense with id {expense_id} not found")
    for key, value in expense_update.dict(exclude_unset=True).items():
        setattr(db_expense, key, value)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@app.delete("/expenses/{expense_id}", status_code=status.HTTP_200_OK)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense_query = db.query(models.Expense).filter(models.Expense.id == expense_id)
    if not (expense_in_db := expense_query.first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Expense with id {expense_id} not found")
    expense_query.delete()
    db.commit()
    return {"detail": f"Expense with id {expense_id} deleted"}