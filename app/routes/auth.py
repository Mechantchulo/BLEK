from flask import Blueprint, request, jsonify
from app import db
from app.models.user_model import User
from app.models.client import Client
from app.models.hardware import Hardware
from app.models.contractor import Contractor
from app.models.professional import Professional
from app.models.fundi import Fundi
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    role = data.get('role')

    try:
        user = User(
            username=data['username'],
            email=data['email'],
            role=role,
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.flush()  # Gives us the user.id before commit

        # Create role-specific profile
        if role == 'customer':
            client_type = data.get('client_type')  # individual or organization
            organization_name = data.get('organization_name') if client_type == 'organization' else None
            client = Client(user_id=user.id, customer_type=client_type, organization_name=organization_name)
            db.session.add(client)

        elif role == 'contractor':
            contractor = Contractor(user_id=user.id)
            db.session.add(contractor)

        elif role == 'professional':
            professional = Professional(user_id=user.id)
            db.session.add(professional)

        elif role == 'fundi':
            fundi = Fundi(user_id=user.id)
            db.session.add(fundi)

        elif role == 'hardware':
            hardware = Hardware(user_id=user.id)
            db.session.add(hardware)

        else:
            return jsonify({'error': 'Invalid role'}), 400

        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email or username already exists.'}), 409

#login route

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        access_token = create_access_token(
            identity={'id': user.id, 'role': user.role},
            expires_delta=timedelta(days=1)
        )
        return jsonify({'access_token': access_token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401


#getting the current user
@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    identity = get_jwt_identity()
    user = User.query.get(identity['id'])

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    }), 200