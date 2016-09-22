from ..extensions import db
from base import Base
from flask_security import RoleMixin

class Role(Base, RoleMixin):
    """Create roles in the database."""

    __tablename__ = 'auth_role'
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        """Initialize the Role object."""
        self.name = name

    def __repr__(self):
        """String representation of the class."""
        return '<Role %r>' % self.name
