# Calorie Prediction App

This Flask web application predicts the number of calories burned during exercise based on various user inputs such as gender, age, height, weight, duration, heart rate, and body temperature.



![App Demo](./path_to_your_gif.gif)

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

### Adding a GIF to README.md

To showcase the app, create a GIF demo:

1. Use a tool like **LiceCap** or **ScreenToGif** to record your web app's interaction.
2. Save the GIF in your `Calorie_prediction_app` directory.
3. Add the GIF to your `README.md` by updating this line:

   ```markdown
   ![App Demo](./path_to_your_gif.gif)
   ```

   Replace `path_to_your_gif.gif` with the relative path to the GIF, e.g., `./demo.gif`.
