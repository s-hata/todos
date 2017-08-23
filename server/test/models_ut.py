import unittest

from app import ( db, app )
from app.models import Todo


class TodoTestCase(unittest.TestCase):

    def setUp(self):
        self.session = db.session

    def tearDown(self):
        self.session.rollback()

    def test_create(self):
        todo = Todo(title='test', complete=False)
        self.session.add(todo)
        result = Todo.query.filter_by(title='test').first()
        self.assertEqual(result.title, 'test')
        self.assertFalse(result.complete)

    def test_update(self):
        todo = Todo(title='test', complete=False)
        self.session.add(todo)
        todo.complete = True
        self.session.add(todo)
        result = Todo.query.filter_by(title='test').first()
        self.assertEqual(result.title, 'test')
        self.assertTrue(result.complete)

    def test_delete(self):
        todo = Todo(title='test', complete=False)
        self.session.add(todo)
        created_todo = Todo.query.filter_by(title='test').first()
        self.session.delete(created_todo)
        result = Todo.query.filter_by(title='test').first()
        self.assertIsNone(result)
