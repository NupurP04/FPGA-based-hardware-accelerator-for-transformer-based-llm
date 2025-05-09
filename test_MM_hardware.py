"from pynq import Overlay
from MM import *
import numpy as np
import time

# Load bitstream
overlay = Overlay('MM.bit')

# Initialize accelerator
ini_MM()

# Create matrices
shape = (160, 160)
A = mat_create(shape)
B = mat_create(shape)
C = mat_create(shape)

# Set input data
A_data = np.random.randint(-128, 128, size=shape, dtype=np.int8)
B_data = np.random.randint(-128, 128, size=shape, dtype=np.int8)
mat_setValue(A, A_data)
mat_setValue(B, B_data)
shift = 10

# Measure timing over multiple runs
num_runs = 10
hardware_times = []
for i in range(num_runs):
    start_time = time.time()
    mat_mul(A, B, C, shift)
    end_time = time.time()
    hardware_times.append(end_time - start_time)

avg_hardware_time = sum(hardware_times) / num_runs
avg_hardware_time_us = avg_hardware_time * 1_000_000
print(f"\nComputation: {avg_hardware_time_us:.2f} usec") 
