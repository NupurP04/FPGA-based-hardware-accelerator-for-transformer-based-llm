import numpy as np
import time

# Input vector
X = np.random.randint(-128, 128, size=(160,),
                      dtype=np.int32).astype(np.float32)

# Optional learnable parameters (usually learned during training)
gamma = np.ones_like(X)
beta = np.zeros_like(X)

start_time = time.perf_counter()

mean = np.mean(X)
variance = np.var(X)
epsilon = 1e-5

layernorm_out = gamma * (X - mean) / np.sqrt(variance + epsilon) + beta

end_time = time.perf_counter()
print("LayerNorm computation time: {:.3f} ms".format(
    (end_time - start_time) * 1e3))
