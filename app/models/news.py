from app import db
from datetime import datetime

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    url = db.Column(db.String(500))
    published_date = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.String(100))

    def __repr__(self):
        return f'<News {self.title}>'
