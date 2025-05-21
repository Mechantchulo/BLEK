from app import db

class Client(db.Model):
    __tablename__ = 'client'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    client_type = db.Column(db.String(100), nullable=False)
    organization_name = db.Column(db.String(100))
    
    # Relationships
    user = db.relationship("User", back_populates="client")