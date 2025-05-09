from pynq import Overlay
from GELU import *  
import numpy as np
import time

# Load bitstream
overlay = Overlay('GELU.bit')

# Initialize accelerator
ini_GELU()

# Create input and output matrices
shape = (160, 160)  # 160x160 matrix
input_matrix = vec_create(shape)  # Input: activations
output_matrix = vec_create(shape)  # Output: GELU activations

# Set input data
input_data = np.random.randint(-128, 128, size=shape, dtype=np.int8)  # int8 input
vec_setValue(input_matrix, input_data)

# Measure timing over multiple runs
num_runs = 10
hardware_times = []
for i in range(num_runs):
    start_time = time.time()
    gelu(input_matrix, output_matrix)  # Apply GELU element-wise
    end_time = time.time()
    hardware_times.append(end_time - start_time)


avg_hardware_time = sum(hardware_times) / num_runs
avg_hardware_time_us = avg_hardware_time * 1_000_000
print(f"\nGeLU computation time: {avg_hardware_time:.2f} usec")
