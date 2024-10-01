from flask import Flask, request, render_template, flash
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

# Load the model
model = joblib.load('calorie_prediction_model.joblib')

# Function to validate inputs
def validate_input(gender, age, height, weight, duration, heart_rate, body_temp):
    errors = []

    # Validate gender
    if gender.lower() not in ['male', 'female']:
        errors.append("Invalid gender. Please enter 'male' or 'female'.")

    # Validate age
    if age <= 0 or age > 120:
        errors.append("Age must be between 1 and 120.")

    # Validate height
    if height <= 0 or height > 300:
        errors.append("Height must be a positive number between 1 and 300 cm.")

    # Validate weight
    if weight <= 0 or weight > 500:
        errors.append("Weight must be a positive number between 1 and 500 kg.")

    # Validate duration
    if duration <= 0 or duration > 1000:
        errors.append("Duration must be a positive number between 1 and 1000 minutes.")

    # Validate heart rate
    if heart_rate <= 0 or heart_rate > 250:
        errors.append("Heart rate must be between 1 and 250 bpm.")

    # Validate body temperature
    if body_temp < 35 or body_temp > 42:
        errors.append("Body temperature must be between 35°C and 42°C.")

    return errors

@app.route('/', methods=['GET', 'POST'])
def predict_calories():
    # Initialize input values
    input_values = {
        'gender': '',
        'age': '',
        'height': '',
        'weight': '',
        'duration': '',
        'heart_rate': '',
        'body_temp': ''
    }

    if request.method == 'POST':
        # Get input from form
        gender = request.form.get('gender', '').strip()
        age = request.form.get('age', '').strip()
        height = request.form.get('height', '').strip()
        weight = request.form.get('weight', '').strip()
        duration = request.form.get('duration', '').strip()
        heart_rate = request.form.get('heart_rate', '').strip()
        body_temp = request.form.get('body_temp', '').strip()

        # Preserve user inputs
        input_values = {
            'gender': gender,
            'age': age,
            'height': height,
            'weight': weight,
            'duration': duration,
            'heart_rate': heart_rate,
            'body_temp': body_temp
        }

        # Initialize errors list
        errors = []

        # Attempt to convert inputs to float where necessary
        try:
            age_val = float(age)
            height_val = float(height)
            weight_val = float(weight)
            duration_val = float(duration)
            heart_rate_val = float(heart_rate)
            body_temp_val = float(body_temp)
        except ValueError:
            flash("All inputs must be valid numbers.")
            return render_template('index.html', errors=[], input_values=input_values)

        # Validate inputs
        errors = validate_input(gender, age_val, height_val, weight_val, duration_val, heart_rate_val, body_temp_val)

        if errors:
            for error in errors:
                flash(error)
            return render_template('index.html', errors=errors, input_values=input_values)

        # Convert gender to numeric (1 for female, 0 for male)
        gender_numeric = 1 if gender.lower() == 'female' else 0

        # Create a DataFrame with the input data
        input_data = pd.DataFrame([[gender_numeric, age_val, height_val, weight_val, duration_val, heart_rate_val, body_temp_val]],
                                  columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])

        # Make prediction
        prediction = model.predict(input_data)[0]

        return render_template('result.html', prediction=round(prediction, 2))

    # For GET request, initialize empty input values
    return render_template('index.html', errors=[], input_values=input_values)

if __name__ == '__main__':
    app.run(debug=True)
