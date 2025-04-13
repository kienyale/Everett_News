from app import db
from datetime import datetime

class Legislation(db.Model):
    __tablename__ = 'legislation'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50))  # ordinance, resolution, etc.
    status = db.Column(db.String(50))  # proposed, approved, rejected, deferred
    introduction_date = db.Column(db.DateTime, default=datetime.utcnow)
    vote_date = db.Column(db.DateTime, nullable=True)
    yes_votes = db.Column(db.Integer, default=0)
    no_votes = db.Column(db.Integer, default=0)
    abstain_votes = db.Column(db.Integer, default=0)
    document_url = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f'<Legislation {self.title}>' 