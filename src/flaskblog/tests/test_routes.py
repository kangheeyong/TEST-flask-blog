from flaskblog import app


def test_response_200():
    response = app.test_client().get('/')
    assert response.status_code == 200

    response = app.test_client().get('/home')
    assert response.status_code == 200

    response = app.test_client().get('/about')
    assert response.status_code == 200

    response = app.test_client().get('/login')
    assert response.status_code == 200

    response = app.test_client().post('/login')
    assert response.status_code == 200

    response = app.test_client().get('/register')
    assert response.status_code == 200

    response = app.test_client().post('/register')
    assert response.status_code == 200

