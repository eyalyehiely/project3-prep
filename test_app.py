from app import get_services
import json,requests
def test_get_services():
    services = json.loads(get_services())["services"]
    length = json.loads(get_services())["length"]
    assert len(services) == length and (services is not None or length is not None)

TEST_URL = 'http://127.0.0.1:5000/api/services'
def test_add_services():
   status = requests.post(url=TEST_URL,json=json.dumps({'services':[]})).json()['status']
   length = requests.post(url=TEST_URL,json=json.dumps({'services':[]})).json()['length']
   
   assert length==0 and status =='ok'