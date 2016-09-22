from ..extensions import db

class Base(db.Model):
    """Base class for all the tables.

    Consists of two default columns `created_at` and `modified_at` .
    """

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime,
                            default=db.func.current_timestamp(),
                            onupdate=db.func.current_timestamp())
                            
