from app import db

class Hardware(db.Model):
    __tablename__ = 'hardware'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    hardware_type = db.Column(db.String(100), nullable=False)
    store_name = db.Column(db.String(100), nullable=False)
    store_location = db.Column(db.String(100), nullable=False)
    # Relationships
    user = db.relationship("User", back_populates="hardware")