from app import db

class Fundi(db.Model):
    __tablename__ = 'fundi'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    speciality = db.Column(db.String(100), nullable=False)
    
    # Relationships
    user = db.relationship("User", back_populates="fundi")