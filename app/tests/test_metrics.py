from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_metrics_endpoint():
    client.get("/expenses")
    client.get("/expenses")

    r = client.get("/metrics")
    assert r.status_code == 200
    assert "expense_api_requests_total" in r.text
    assert r.headers["content-type"].startswith("text/plain")