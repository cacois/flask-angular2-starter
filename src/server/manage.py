from flask_script import Manager
from flask_app.app import app
from flask_app.extensions import db

print('Initializing Manager...')
manager = Manager(app)

@manager.command
def runserver():
    """Run the flask app in development mode"""
    app.run('0.0.0.0', 8081)

@manager.command
def initdb():
    """Drops exising schema and recreates all tables"""
    print('dropping old schema...')
    db.drop_all()
    print('create tables...')
    db.create_all()

@manager.command
def list_users():
    """lists all users currently in the db"""
    from flask_app.models import User
    print(User.query.all())

@manager.command
def insert_data():
    """Inserts default data into the database, such as an admin user"""
    from flask_app.models import User, Role
    from flask_security import utils, SQLAlchemyUserDatastore

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)

    if not User.query.first():
        user_datastore.create_user(
            email=app.config['ADMIN_USER'],
            password=utils.encrypt_password(app.config['ADMIN_PASSWORD']))
        db.session.commit()

if __name__ == "__main__":
    manager.run()
