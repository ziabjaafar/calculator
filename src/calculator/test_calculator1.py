from fastapi.testclient import TestClient
from calculator1 import app

client = TestClient(app)

def test_can_multiply_Number():
    response = client.post("/multiply/", json={"value": 3.0})
    assert response.status_code == 200
    assert response.json() =={"multiply" : 9.0}

def test_division_Number():
    response=client.post("/division/", json={"value" : 5.0})
    assert response.status_code == 200
    assert response.json() == {"division" : 2.5}

def test_sum_Number():
    response = client.post("/sum/" , json={"value":10.0})
    assert response.status_code == 200
    assert response.json() == {"sum":20.0}
