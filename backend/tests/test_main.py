from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "Telecom Cloud Platform"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_ready():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_metrics():
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "telecom_api_requests_total" in response.text


def test_metrics_latency():
    response = client.get("/health")

    assert response.status_code == 200

    metrics = client.get("/metrics")

    assert metrics.status_code == 200
    assert "telecom_api_request_duration_seconds" in metrics.text
