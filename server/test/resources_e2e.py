import unittest
import json

from app import ( app, db )
from app.models import Todo

http_headers={
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiU2l0ZVBvaW50IFJlYWRlciJ9.sS4aPcmnYfm3PQlTtH14az9CGjWkjnsDyG_1ats4yYg'
}

class TodoResourceTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.session = db.session

    def tearDown(self):
        self.session.query(Todo).delete()
        self.session.commit()
        reset()

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

        todo = Todo(title='test', complete=False)
        self.session.add(todo)
        self.session.commit()

        body = {
            'title': u'test',
            'complete': True,
        }

        json_body = json.dumps(body)
        response = self.client.put('todos/1',
                                    data=json_body,
                                    headers=http_headers
                                    )
        self.assertEquals(200, response.status_code)

    def test_delete_success(self):

        todo = Todo(title='test', complete=False)
        self.session.add(todo)
        self.session.commit()

        response = self.client.delete('todos/1',
                                    headers=http_headers
                                    )
        self.assertEquals(200, response.status_code)


def reset():
    db.engine.execute('alter table todo auto_increment=1')
