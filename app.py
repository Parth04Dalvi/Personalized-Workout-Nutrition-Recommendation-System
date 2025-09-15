from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db' # Use a different database for production
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    height_cm = db.Column(db.Float)
    weight_kg = db.Column(db.Float)
    activity_level = db.Column(db.String(20)) # e.g., 'sedentary', 'moderately_active'
    goal = db.Column(db.String(20)) # e.g., 'weight_loss', 'muscle_gain'

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    muscle_group = db.Column(db.String(50))
    equipment = db.Column(db.String(50))
    difficulty = db.Column(db.String(20)) # e.g., 'beginner', 'intermediate'

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer)
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fats = db.Column(db.Float)

# Create tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
