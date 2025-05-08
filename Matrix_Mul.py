import numpy as np
import time

# Define matrix dimensions and shift value
MATRIX_DIM = (160, 160)
shift = 10

# Create random matrices with integer values between -128 and 127
# Using np.int32 to avoid overflow during multiplication
A = np.random.randint(-128, 128, MATRIX_DIM, dtype=np.int32)
B = np.random.randint(-128, 128, MATRIX_DIM, dtype=np.int32)

# Start timing the computation
start_time = time.perf_counter()

# Perform the matrix multiplication in software
C_soft = np.matmul(A, B)
# Apply a right-shift with rounding
C_soft = np.right_shift(C_soft + (1 << (shift - 1)), shift)
# Clip the results to 8-bit signed values and convert to np.int8
C_soft = np.clip(C_soft, -128, 127).astype(np.int8)

# Stop timing
end_time = time.perf_counter()
elapsed_time = (end_time - start_time) * 1e3  # Convert to milliseconds

print("Software computation time: {:.3f} ms".format(elapsed_time))
