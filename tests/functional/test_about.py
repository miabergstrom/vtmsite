import app
from app import estimate

def test_index_route(app,client):
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Welcome to VTM!" in res.data

def test_about_route(app,client):
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Vertical Tank Maintenance" in res.data
        assert b"Company Information" in res.data
        assert b"Address:" in res.data
        assert b"Phone Number:" in res.data
        assert b"Email:" in res.data
        assert b"Company History" in res.data


def test_estimate_route(app,client):
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200 #get
        assert b"VTM Estimator" in res.data
        assert b"Estimate Total Cost:" in res.data
        assert b"Input measurements in inches" in res.data

