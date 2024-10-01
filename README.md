# Calorie Prediction App

This Flask web application predicts the number of calories burned during exercise based on various user inputs such as gender, age, height, weight, duration, heart rate, and body temperature.



![App Demo](./Calorie%20Burn%20Prediction/calorie_prediction_app/ScreenRecording2024-10-02at12.05.00AM-ezgif.com-speed.gif)

## Features

- Easy-to-use web interface
- Validates input data
- Predicts calories burned based on a trained machine learning model

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/monkeydcoder/Calorie-Prediction-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Calorie_prediction_app
   ```

3. Create and activate a virtual environment (if you haven't already):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python app.py
   ```

   The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

Once the app is running, open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/). Fill out the form with your details, and the app will predict how many calories you burned based on the inputs provided.

## Folder Structure

```
Calorie_prediction_app/
│
├── __pycache__/
├── templates/
│   ├── index.html
│   ├── result.html
├── venv/
├── app.py
├── calorie_prediction_model.joblib
├── requirements.txt
├── README.md
└── model_calorie_burn_prediction.ipynb
```

## Contributing

Feel free to submit pull requests or report issues. Contributions are always welcome!

## License

This project is licensed under the MIT License.
