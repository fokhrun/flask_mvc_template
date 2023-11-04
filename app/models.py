
""" Models for the template application"""

from . import db
from enum import Enum


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref="role", lazy="dynamic")

    def __repr__(self):
        return f"<Role: {self.name}>"


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self) -> str:
        return f"<User: {self.username}>"


class TableCapacity(Enum):
    two = 2
    four = 4
    six = 6


class ReservationSlot(Enum):
    evening = 1
    night = 2


class Table(db.Model):
    __tablename__ = "tables"
    id = db.Column(db.Integer, primary_key=True)
    table_capacity = db.Column(db.Enum(TableCapacity), nullable=False)
    reservations = db.relationship('Reservation', backref="table", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<Table: {self.id}, Capacity: {self.table_capacity.value}>"


class Reservation(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey("tables.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    reservation_time_slot = db.Column(db.Enum(ReservationSlot), nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    reservation_status = db.Column(db.Boolean, nullable=False, default=False)
    
    def __repr__(self) -> str:
        return f"<Reservations: Table: {self.table_id}, User: {self.user_id}, Slot: {self.reservation_time_slot.name}, Date: {self.reservation_date}>"
