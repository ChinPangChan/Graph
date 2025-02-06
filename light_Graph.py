import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read data
light_data = pd.read_csv("LightData.csv")
light_data = light_data[['time', 'light', 'sensor']]

# Step 2: Fix time format
light_data['time'] = pd.to_datetime(light_data['time'])

# Step 3: Create plot
plt.figure(figsize=(10, 5))

# Draw lines for each sensor
for sensor_name, sensor_group in light_data.groupby('sensor'):
    plt.plot(
        sensor_group['time'], 
        sensor_group['light'], 
        label=f'Sensor {sensor_name}'
    )

# Add labels and style
plt.xlabel('Time')
plt.ylabel('Light Level')
plt.title('Light Levels by Sensor')
plt.legend()
plt.grid(True)

# Save and show
plt.savefig('light_plot.png')
plt.show()

print("Light plot saved as light_plot.png")