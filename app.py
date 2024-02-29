from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Product, Test
from cli_commands import read_products,read_tests  # Import the custom command

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

migrate = Migrate(app, db)
app.cli.add_command(read_products)
app.cli.add_command(read_tests)



