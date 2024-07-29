import pandas as pd
import matplotlib.pyplot as plt

# Load network traffic data (example format: time, traffic_in, traffic_out)
data = pd.read_csv('network_traffic.csv')

# Basic statistics
print(data.describe())

# Plotting traffic data
plt.figure(figsize=(12, 6))
plt.plot(data['time'], data['traffic_in'], label='Traffic In')
plt.plot(data['time'], data['traffic_out'], label='Traffic Out')
plt.xlabel('Time')
plt.ylabel('Traffic (Mbps)')
plt.title('Network Traffic Analysis')
plt.legend()
plt.grid(True)
plt.show()
