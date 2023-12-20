from flask import Flask, jsonify, render_template, request
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

app = Flask(__name__)

vals = {0:'None',1:'a',2:'e'}
latest = 'None'

i = 0

my_model = tf.keras.models.load_model("my_model")
sc = StandardScaler()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/receive_sensor_data', methods=['POST'])
def receive_sensor_data():
    data = request.json
    save_to_csv(data)
    return 'Sensor data received and saved successfully!'

def save_to_csv(data):
    global i
    with open('data_e/sensor_data'+str(i)+'.csv', 'w') as csvfile:
        csvfile.write("timestamp,x,y,z\n")
        i+=1
        for entry in data:
            row = f"{entry['timestamp']},{entry['x']},{entry['y']},{entry['z']}\n"
            csvfile.write(row)


@app.route('/predict_drawing', methods=['POST'])
def receive_data():
    data = request.json
    # print(data)
    global latest
    X=[]
    for entry in data:
        X.append([entry['timestamp'],entry['x'],entry['y'],entry['z']])
    data = np.array(X[:300])
    t_scaled = sc.fit_transform(data).reshape(30,10,-1)
    print(vals[np.argmax(my_model.predict(np.array([t_scaled])))])
    latest=vals[np.argmax(my_model.predict(np.array([t_scaled])))]
    # print(latest)

    return 'Sensor data received and saved successfully!'

@app.route('/get_pred')
def return_prediction():
    global latest
    return jsonify(variable=latest)


if __name__ == '__main__':
    app.run()
