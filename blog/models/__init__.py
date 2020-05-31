from flask_sqlalchemy import SQLAlchemy
from flask import Flask, current_app
from ..__init__ import get_db

db = get_db()