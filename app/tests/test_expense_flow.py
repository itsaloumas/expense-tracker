from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_get_delete_expense():
    expense_data = {
        "description": "Test Expense",
        "amount": 100.50,
        "category": "Test Category"
    }
    
    create_response = client.post("/expenses", json=expense_data)
    assert create_response.status_code == 201, f"Expected status code 201, got {create_response.status_code}"
    created_expense = create_response.json()

    assert "id" in created_expense, "Created expense should contain 'id'."
    expense_id = created_expense["id"]
    assert created_expense["description"] == expense_data["description"]
    assert created_expense["amount"] == expense_data["amount"]
    assert created_expense["category"] == expense_data["category"]

    get_response = client.get(f"/expenses/{expense_id}")
    assert get_response.status_code == 200, f"Expected status code 200, got {get_response.status_code}"
    fetched_expense = get_response.json()
    assert fetched_expense["id"] == expense_id
    assert fetched_expense["description"] == expense_data["description"]

    delete_response = client.delete(f"/expenses/{expense_id}")
    assert delete_response.status_code == 200, f"Expected status code 200, got {delete_response.status_code}"
    delete_data = delete_response.json()
    assert "detail" in delete_data, "Delete response should have a 'detail' key."

    get_after_delete = client.get(f"/expenses/{expense_id}")
    assert get_after_delete.status_code == 404, f"Expected status code 404 after deletion, got {get_after_delete.status_code}"
