from flask import Flask,request, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from config import ApplicationConfig
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS



from models import db, User


app = Flask(__name__)

app.config.from_object(ApplicationConfig)

migrate = Migrate(app=app, db=db)

db.init_app(app=app)
jwt = JWTManager(app=app)
bcrypt = Bcrypt(app=app)
api = Api(app=app)
CORS(app=app)

class Signup(Resource):
    def post(self):
        email = request.get_json()['email']
        password = request.get_json()['password']

        newUser = User(
            email=email,
            password=bcrypt.generate_password_hash(password)
        )

        db.session.add(newUser)
        db.session.commit()

        response = make_response(jsonify(newUser.to_dict()), 201)
        return response
    
class Login(Resource):
    def post(self):
        email = request.get_json()['email']
        password = request.get_json()['password']

        user = User.query.filter_by(email=email).first()

        if not user:
            return {"error": "User not found"},401
        
        if not bcrypt.check_password_hash(user.password, password):
            return {"error": "credentials do not match"}, 401
        
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token)
    
api.add_resource(Signup, "/signup", endpoint="signup")
api.add_resource(Login, "/login", endpoint="login")


if __name__ == "__main__":
    app.run(port=5555, debug=True)