import numpy as np

# Parameters for the optimization
num_cells = 10
num_channels = 5

# Generate random signal strengths (in dBm) for each cell and channel
np.random.seed(42)
signal_strengths = np.random.uniform(-100, -50, (num_cells, num_channels))

# Function to calculate the interference for a given channel allocation
def calculate_interference(allocation):
    interference = 0
    for i in range(num_cells):
        for j in range(i + 1, num_cells):
            if allocation[i] == allocation[j]:
                interference += signal_strengths[i][allocation[i]] + signal_strengths[j][allocation[j]]
    return interference

# Initial allocation of channels (random)
channel_allocation = np.random.randint(0, num_channels, num_cells)
initial_interference = calculate_interference(channel_allocation)

print(f"Initial channel allocation: {channel_allocation}")
print(f"Initial interference: {initial_interference} dBm")

# Optimize channel allocation to minimize interference
# (Using a simple hill-climbing approach for demonstration)
for i in range(1000):  # Number of iterations
    new_allocation = channel_allocation.copy()
    cell_to_change = np.random.randint(0, num_cells)
    new_allocation[cell_to_change] = np.random.randint(0, num_channels)
    new_interference = calculate_interference(new_allocation)
    if new_interference < initial_interference:
        channel_allocation = new_allocation
        initial_interference = new_interference

print(f"Optimized channel allocation: {channel_allocation}")
print(f"Optimized interference: {initial_interference} dBm")
