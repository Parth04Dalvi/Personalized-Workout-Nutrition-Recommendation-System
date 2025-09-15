# logic.py
def calculate_bmr(user):
    """Calculates Basal Metabolic Rate using the Mifflin-St Jeor equation."""
    if user.gender.lower() == 'male':
        return (10 * user.weight_kg) + (6.25 * user.height_cm) - (5 * user.age) + 5
    else: # female
        return (10 * user.weight_kg) + (6.25 * user.height_cm) - (5 * user.age) - 161

def calculate_tdee(user):
    """Calculates Total Daily Energy Expenditure."""
    bmr = calculate_bmr(user)
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'extremely_active': 1.9
    }
    return bmr * activity_multipliers.get(user.activity_level.lower(), 1.2)

def generate_workout_plan(user):
    """Generates a workout plan based on user's goal."""
    if user.goal == 'muscle_gain':
        return [
            {'exercise': 'Squats', 'sets': 4, 'reps': 6},
            {'exercise': 'Bench Press', 'sets': 4, 'reps': 8},
            {'exercise': 'Pull-ups', 'sets': 3, 'reps': 10},
        ]
    elif user.goal == 'weight_loss':
        return [
            {'exercise': 'Running (30 min)', 'sets': 1, 'reps': None},
            {'exercise': 'HIIT (20 min)', 'sets': 1, 'reps': None},
            {'exercise': 'Push-ups', 'sets': 3, 'reps': 12},
        ]
    else:
        return []

def generate_nutrition_plan(user):
    """Generates nutrition targets based on TDEE and goal."""
    tdee = calculate_tdee(user)
    calories = tdee
    if user.goal == 'weight_loss':
        calories -= 500
    elif user.goal == 'muscle_gain':
        calories += 300

    protein = calories * 0.35 / 4 # 35% of calories from protein (4 kcal/g)
    carbs = calories * 0.40 / 4 # 40% of calories from carbs
    fats = calories * 0.25 / 9 # 25% of calories from fats (9 kcal/g)

    return {
        'calories': round(calories, 2),
        'protein_g': round(protein, 2),
        'carbs_g': round(carbs, 2),
        'fats_g': round(fats, 2)
    }
