from flask.testing import FlaskClient

def test_registration(client: FlaskClient):
    result = client.post("/auth/register", json={"username":"test1", "email":"test@test.com","password":"password"})
    assert result.status_code == 201

def test_login(client: FlaskClient):
    result = client.post("/auth/token", json={"username":"test1", "password":"password"})
    assert result.status_code == 200
