from app import db

class Professional(db.Model):
    __tablename__ = 'professional'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    certification_file = db.Column(db.String(100), nullable=False)
    portfolio_images = db.Column(db.JSON)
    is_verified = db.Column(db.Boolean, default=False)

    user = db.relationship("User", back_populates="professional")

    
    
