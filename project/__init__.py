from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager

# init SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    secret = secrets.token_urlsafe(32)
    # app.secret_key = secret
    app.config['SECRET_KEY'] = secret
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    if __name__ == "__main__":
        app.run(debug=False, host='0.0.0.0', port=5000)


    return app



