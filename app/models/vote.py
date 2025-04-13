from app import db
from datetime import datetime

class Vote(db.Model):
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    legislation_id = db.Column(db.Integer, db.ForeignKey('legislation.id'), nullable=False)
    councilor_id = db.Column(db.Integer, db.ForeignKey('councilors.id'), nullable=False)
    vote = db.Column(db.String(10), nullable=False)  # yes, no, abstain
    vote_date = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return f'<Vote {self.id} on legislation {self.legislation_id}>' 