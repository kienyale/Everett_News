from app import db
from datetime import datetime

class Meeting(db.Model):
    __tablename__ = 'meetings'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    start_time = db.Column(db.String(20), nullable=True)
    end_time = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    agenda_url = db.Column(db.String(255), nullable=True)
    minutes_url = db.Column(db.String(255), nullable=True)
    video_url = db.Column(db.String(255), nullable=True)
    is_special = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(50), default='scheduled')  # scheduled, completed, cancelled
    
    def __repr__(self):
        return f'<Meeting {self.title} on {self.date}>' 