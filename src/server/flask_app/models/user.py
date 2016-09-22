from ..extensions import db
from base import Base
from flask_security import UserMixin

# linker table
roles_users = db.Table('roles_users',
                db.Column('user_id', db.Integer(),
                db.ForeignKey('auth_user.id')),
                db.Column('role_id', db.Integer(),
                db.ForeignKey('auth_role.id'))
                )

class User(Base, UserMixin):
    """Create users in the database."""

    __tablename__ = 'auth_user'
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role',
                            secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        """String representation of the class."""
        return '<User %r>' % self.email
