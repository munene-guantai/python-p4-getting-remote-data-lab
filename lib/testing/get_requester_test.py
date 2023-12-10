import json
from GetRequester import GetRequester
class GetRequesterTest:
    '''Class {Classname} in {modulename}.py'''
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = '[{"name":"Daniel","occupation":"LG Fridge Salesman"},{"name":"Joe","occupation":"WiFi Fixer"},{"name":"Avi","occupation":"DJ"},{"name":"Howard","occupation":"Mountain Legend"}]'
CONVERTED_DATA = [
    {'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
    {'name': 'Joe', 'occupation': 'WiFi Fixer'},
    {'name': 'Avi', 'occupation': 'DJ'},
    {'name': 'Howard', 'occupation': 'Mountain Legend'}
]

def test_get_response():
        '''get_response_body function returns response.'''
        requester = GetRequester(URL)
        response_body = requester.get_response_body()

        expected_data = json.loads(JSON_STRING)

        actual_data = json.loads(response_body)

        assert actual_data == expected_data

def test_load_json():
        '''load_json function returns response.'''
        requester = GetRequester(URL)
        assert(requester.load_json() == CONVERTED_DATA)
