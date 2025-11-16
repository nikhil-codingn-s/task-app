from app import app


def test_index():
client = app.test_client()
r = client.get('/')
assert r.status_code == 200
j = r.get_json()
assert 'status' in j and j['status'] == 'ok'
