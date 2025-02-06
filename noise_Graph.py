import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read data
noise_data = pd.read_csv("NoiseData.csv")
noise_data = noise_data[['time', 'noise', 'sensor']]

# Step 2: Fix time format
noise_data['time'] = pd.to_datetime(noise_data['time'])

# Step 3: Create plot
plt.figure(figsize=(10, 5))

# Draw dashed lines for each sensor
for sensor_name, sensor_group in noise_data.groupby('sensor'):
    plt.plot(
        sensor_group['time'], 
        sensor_group['noise'], 
        linestyle='--',  # Dashed line
        label=f'Sensor {sensor_name}'
    )

# Add labels and style
plt.xlabel('Time')
plt.ylabel('Noise Level (dB)')
plt.title('Noise Levels by Sensor')
plt.legend()
plt.grid(True)

# Save and show
plt.savefig('noise_plot.png')
plt.show()

print("Noise plot saved as noise_plot.png")