import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load accelerometer data from CSV

for i in range(4,15):
    data = pd.read_csv(f'data_noisy/sensor_data{i}.csv')

    # Constants
    time_interval = 0.016  # Time interval between accelerometer readings (in seconds)

    # Initialize variables
    velocity = np.zeros((len(data), 3))     # Initialize velocity array with zeros
    displacement = np.zeros((len(data), 3)) # Initialize displacement array with zeros
    accn = [data['x'],data['y'],data['z']]
    # Process accelerometer data
    for i in range(1, len(data)):
        # Integrate acceleration to obtain velocity
        # accn=[i]=[data[i].x,data[i].y,data[i].z]
        velocity[i] = velocity[i-1] + data[['x', 'y', 'z']].iloc[i] * 0.16
        
        # Integrate velocity to obtain displacement
        displacement[i] =  velocity[i-1] * 0.16 + 0.5*data[['x', 'y', 'z']].iloc[i] * 0.16 *0.16

    # Plot displacement
    time = data['timestamp']  
    plt.figure(figsize=(10, 6))
    plt.plot(time,displacement[:, 0][:])
    plt.plot(time,displacement[:, 1][:])
    plt.plot(time,displacement[:, 2][:])


    plt.xlabel('Time (seconds)')
    plt.ylabel('Displacement (meters)')
    plt.title('Displacement Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


