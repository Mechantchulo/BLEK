from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), unique=True, nullable=False)
    lastname = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

    role = db.Column(db.String(100), nullable=False)
    
    # Relationships
    client = db.relationship("Client", uselist=False, back_populates="user")
    fundi = db.relationship("Fundi", uselist=False, back_populates="user")
    contractor = db.relationship("Contractor", uselist=False, back_populates="user")
    professional = db.relationship("Professional", uselist=False, back_populates="user")
    hardware = db.relationship("Hardware", uselist=False, back_populates="user")
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.role}')"
