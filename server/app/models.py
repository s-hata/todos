from app import db
from app.mixin import JsonMixin

class Todo(db.Model, JsonMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    complete = db.Column(db.Boolean)

    props = [
        'id',
        'title',
        'complete'
    ]
