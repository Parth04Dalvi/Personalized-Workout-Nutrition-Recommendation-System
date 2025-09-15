# seed_db.py
from app import app, db, Exercise, Food

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Add some exercises
        exercises = [
            {'name': 'Squats', 'description': 'Targets legs and glutes.', 'muscle_group': 'legs', 'equipment': 'barbell', 'difficulty': 'intermediate'},
            {'name': 'Bench Press', 'description': 'Targets chest and triceps.', 'muscle_group': 'chest', 'equipment': 'barbell', 'difficulty': 'intermediate'},
            {'name': 'Pull-ups', 'description': 'Targets back and biceps.', 'muscle_group': 'back', 'equipment': 'pull-up bar', 'difficulty': 'hard'},
            {'name': 'Running', 'description': 'Cardiovascular exercise.', 'muscle_group': 'cardio', 'equipment': 'none', 'difficulty': 'easy'},
            {'name': 'Push-ups', 'description': 'Targets chest, shoulders, and triceps.', 'muscle_group': 'chest', 'equipment': 'none', 'difficulty': 'easy'},
            {'name': 'Deadlifts', 'description': 'Full-body compound exercise.', 'muscle_group': 'full_body', 'equipment': 'barbell', 'difficulty': 'hard'},
        ]

        for ex_data in exercises:
            exercise = Exercise(**ex_data)
            db.session.add(exercise)

        # Add some foods
        foods = [
            {'name': 'Chicken Breast', 'calories': 165, 'protein': 31, 'carbs': 0, 'fats': 3.6},
            {'name': 'Brown Rice', 'calories': 123, 'protein': 2.7, 'carbs': 25.6, 'fats': 0.9},
            {'name': 'Broccoli', 'calories': 34, 'protein': 2.8, 'carbs': 6.6, 'fats': 0.4},
            {'name': 'Salmon', 'calories': 208, 'protein': 20, 'carbs': 0, 'fats': 13},
            {'name': 'Sweet Potato', 'calories': 86, 'protein': 1.6, 'carbs': 20, 'fats': 0.1},
            {'name': 'Whey Protein', 'calories': 120, 'protein': 25, 'carbs': 3, 'fats': 2},
        ]

        for food_data in foods:
            food = Food(**food_data)
            db.session.add(food)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
