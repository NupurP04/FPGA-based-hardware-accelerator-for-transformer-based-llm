import numpy as np
import time

# Example input (simulate a transformer attention score matrix)
X = np.random.randint(-128, 128, size=(160,),
                      dtype=np.int32).astype(np.float32)

start_time = time.perf_counter()

# Subtract max for numerical stability
X_max = np.max(X)
e_x = np.exp(X - X_max)
softmax_out = e_x / np.sum(e_x)

end_time = time.perf_counter()
print("Softmax computation time: {:.3f} ms".format(
    (end_time - start_time) * 1e3))
