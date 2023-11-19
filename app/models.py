""" Models for the template application"""

from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


class Role(db.Model):
    """Model for user roles"""

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref="role", lazy="dynamic")

    def __repr__(self):
        return f"<Role: {self.name}>"


class User(UserMixin, db.Model):
    """Model for user accounts"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(512))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    @property
    def password(self):
        """Prevent password from being accessed

        Raises
        ------
            AttributeError
            password is not a readable attribute
        """
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """Set password to a hashed password

        Parameters
        ----------
        password : str
            password to be hashed
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Check if hashed password matches actual password

        Returns
        -------
        bool
            True if the password matches, False otherwise
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User: {self.username}>"


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID

    Parameters
    ----------
    user_id : int
        ID of the user

    Returns
    -------
        User
        User object corresponding to the user_id
    """
    return User.query.get(int(user_id))


class TableCapacity(Enum):
    """Enum for table capacity

    Parameters
    ----------
    Enum : _base
    """
    two = 2  # pylint: disable=invalid-name  # noqa: E501
    four = 4  # pylint: disable=invalid-name  # noqa: E501
    six = 6  # pylint: disable=invalid-name  # noqa: E501


class ReservationSlot(Enum):
    """Enum for reservation slots

    Parameters
    ----------
    Enum : _base
    """
    evening = 1  # pylint: disable=invalid-name  # noqa: E501
    night = 2  # pylint: disable=invalid-name  # noqa: E501


class Table(db.Model):
    """Model for restaurant tables"""

    __tablename__ = "tables"
    id = db.Column(db.Integer, primary_key=True)
    table_capacity = db.Column(db.Enum(TableCapacity), nullable=False)
    reservations = db.relationship('Reservation', backref="table", lazy="dynamic")

    def __repr__(self):
        return f"<Table: {self.id}, Capacity: {self.table_capacity.value}>"


class Reservation(db.Model):
    """Model for table reservations"""

    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey("tables.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reservation_time_slot = db.Column(db.Enum(ReservationSlot), nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    reservation_status = db.Column(db.Boolean, nullable=False, default=False)

    def get_status_string(self):
        """Get status string for a reservation"""
        return "reserved" if self.reservation_status else "unreserved"

    def __repr__(self):
        return f"<Reservation: Table: {self.table_id}, User: {self.user_id}, Slot: {self.reservation_time_slot.name}, Date: {self.reservation_date}>"  # noqa: E501 # pylint: disable=line-too-long
