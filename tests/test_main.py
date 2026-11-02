from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_crear_y_consultar_estudiante():
    datos = {"nombre": "Ana", "apellido": "Pérez", "correo": "ana@correo.com"}
    r = client.post("/students", json=datos)
    assert r.status_code == 201
    creado = r.json()
    assert creado["nombre"] == "Ana"

    r = client.get(f"/students/{creado['id']}")
    assert r.status_code == 200
    assert r.json()["correo"] == "ana@correo.com"


def test_listar_estudiantes():
    r = client.get("/students")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_estudiante_no_existe():
    r = client.get("/students/99999")
    assert r.status_code == 404
