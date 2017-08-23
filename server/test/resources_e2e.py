import unittest
import json

from app import ( app, db )

http_headers={
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiU2l0ZVBvaW50IFJlYWRlciJ9.sS4aPcmnYfm3PQlTtH14az9CGjWkjnsDyG_1ats4yYg'
}

class TodoResourceTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.session = db.session

    def tearDown(self):
        self.session.rollback()

    def test_create_success(self):
        body = {
            'title': u'test',
            'complete': False,
        }

        json_body = json.dumps(body)
        response = self.client.post('todos',
                                    data=json_body,
                                    headers=http_headers
                                    )
        self.assertEquals(201, response.status_code)
        created_todo = json.loads(response.data)
        #json_body = json.loads(json_body)
        #self.assertEquals(json_body['name'], catalog['name'])
        #self.assertEquals(json_body['order'], catalog['order'])
        #self.assertIsNotNone(catalog['created_by'])
        #self.assertIsNotNone(catalog['created_at'])

    def test_update_success(self):
        body = {
            'title': u'test',
            'complete': True,
        }

        json_body = json.dumps(body)
        response = self.client.put('todos',
                                    data=json_body,
                                    headers=http_headers
                                    )
        self.assertEquals(200, response.status_code)
