from app import db

class Councilor(db.Model):
    __tablename__ = 'councilors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    committees = db.Column(db.String(255), nullable=True)
    term_start = db.Column(db.DateTime, nullable=True)
    term_end = db.Column(db.DateTime, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f'<Councilor {self.name}>' 