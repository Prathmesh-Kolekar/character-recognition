# character-recognition
Recognises the characters (Alphabets) through a Neural Network which translates the Accelerometer data from phone to a specific character when in motion

# Mobile Accelerometer to Alphabet Translator

This project involves a Flask web application that receives sensor data from a mobile device's accelerometer and predicts the corresponding alphabet using a trained neural network model.

## Prerequisites

- Flask
- NumPy
- scikit-learn
- TensorFlow

Install the required dependencies using the following command:

```bash
pip install Flask numpy scikit-learn tensorflow
Usage
Run the Flask application:

bash
Copy code
python app.py
Access the application through a web browser at http://127.0.0.1:5000/.

The application provides the following endpoints:

/receive_sensor_data: Receives sensor data from the accelerometer.
/predict_drawing: Uses a trained neural network to predict the corresponding alphabet based on the received sensor data.
/get_pred: Returns the latest prediction.
Project Structure
app.py: Flask application script.
my_model (folder): Contains the trained neural network model.
data_e (folder): Stores CSV files with sensor data.

