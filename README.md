# Personalized Workout & Nutrition Recommendation System

#💡 About the Project
This project is a Personalized Workout & Nutrition Recommendation System designed to help users achieve their fitness goals. By collecting key user data, such as age, weight, height, and fitness goals, the system generates customized workout routines and daily nutrition plans. The core of the application lies in its backend logic, which uses standard metabolic formulas to calculate calorie and macronutrient needs, then recommends an exercise and meal plan tailored to the individual

<img width="845" height="469" alt="image" src="https://github.com/user-attachments/assets/13da0242-ec32-4b04-bde5-6f88b4e009c0" />

✨ Features
User Profile Management: Create and update a personalized profile with all the necessary information.

Dynamic Recommendations: Receive a unique workout and nutrition plan based on your specific goals (e.g., muscle gain, weight loss, maintenance).

Workout Plans: Get a detailed workout routine with recommended exercises, sets, and repetitions.

Nutrition Plans: Receive a breakdown of your daily calorie and macronutrient targets (protein, carbs, fats) and sample meal suggestions.

API Endpoints: A RESTful API to manage user data and fetch recommendations.

💻 Technology Stack
Backend: Python

Web Framework: Flask

Database: SQLAlchemy (ORM) with SQLite (for development)

Dependencies: Flask, Flask-SQLAlchemy

🚀 Installation and Setup
Follow these steps to get the project up and running on your local machine.

Prerequisites
Python 3.8+

pip (Python package installer)

Steps
Clone the repository:

Bash

git clone https://github.com/Parth04Dalvi/Personalized-Workout-Nutrition-Recommendation-System
.git
cd fitness-recommendation-system
Create a virtual environment:
It's highly recommended to use a virtual environment to manage dependencies.

Bash

python -m venv venv
Activate the virtual environment:

On macOS/Linux:

Bash

source venv/bin/activate
On Windows:

Bash

venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
Run the application:

Bash

python app.py
The server will start running, and you can access the API at http://127.0.0.1:5000.

🧪 Usage
You can interact with the API using a tool like Postman or curl.

Create a User
Endpoint: POST /users

Body (JSON):

JSON

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "age": 30,
  "gender": "male",
  "height_cm": 180,
  "weight_kg": 85,
  "activity_level": "moderately_active",
  "goal": "muscle_gain"
}
Get Recommendations
Endpoint: GET /recommendations/<user_id>

Example: GET /recommendations/1

Response (JSON):

JSON

{
  "nutrition_plan": {
    "calories": 2500,
    "protein_g": 218.75,
    "carbs_g": 250.0,
    "fats_g": 69.44
  },
  "user_info": {
    "age": 30,
    "goal": "muscle_gain",
    "name": "John Doe"
  },
  "workout_plan": [
    { "exercise": "Squats", "reps": 6, "sets": 4 },
    { "exercise": "Bench Press", "reps": 8, "sets": 4 },
    { "exercise": "Pull-ups", "reps": 10, "sets": 3 }
  ]
}
