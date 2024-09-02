# models.py 用于定义数据表
from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)


class ThermochemistryDataModel(db.Model):
    __tablename__ = "thermochemistry_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    original_formula = db.Column(db.String(50), nullable=False)
    result_formula = db.Column(db.String(50), nullable=False)
    data_flag = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    units = db.Column(db.String(20), nullable=False)
    method = db.Column(db.String(50), nullable=False)
    reference = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(200), nullable=True)
    label = db.Column(db.String(100), nullable=False)


class ParameterDataModel(db.Model):
    __tablename__ = "parameter_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    data_found = db.Column(db.String(50), nullable=False)
    temperature_range = db.Column(db.String(50), nullable=False)
    A = db.Column(db.Float, nullable=False)
    B = db.Column(db.Float, nullable=False)
    C = db.Column(db.Float, nullable=False)
    D = db.Column(db.Float, nullable=False)
    E = db.Column(db.Float, nullable=False)
    F = db.Column(db.Float, nullable=False)
    G = db.Column(db.Float, nullable=False)
    H = db.Column(db.Float, nullable=False)
    reference = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(200), nullable=True)
    label = db.Column(db.String(100), nullable=False)

    # 外键
    formula_id = db.Column(db.Integer, db.ForeignKey("thermochemistry_data.id"))

    formula = db.relationship(ThermochemistryDataModel, backref="parameter_data")


class DatabaseModel(db.Model):
    __tablename__="database_path"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    database_name = db.Column(db.String(100), nullable=False)
    belonging = db.Column(db.String(100),nullable=False)
