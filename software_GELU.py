import numpy as np
import time

# Input vector
X = np.random.randint(-128, 128, size=(160,),
                      dtype=np.int32).astype(np.float32)

start_time = time.perf_counter()

# GELU approximation (from BERT paper)
gelu_out = 0.5 * X * (1 + np.tanh(np.sqrt(2 / np.pi) *
                      (X + 0.044715 * np.power(X, 3))))

end_time = time.perf_counter()
print("GELU computation time: {:.3f} ms".format((end_time - start_time) * 1e3))
