from pynq import Overlay
from pynq import MMIO
import numpy as np
import time

# Load bitstream
overlay = Overlay("shreeya.bit")  # Use actual filename
ip_base_addr = 0x43C00000
ip_range = 0x1000

ip = MMIO(ip_base_addr, ip_range)

# Offsets (from your control interface)
Q_OFFSET = 0x200
K_OFFSET = 0x400
V_OFFSET = 0x600
OUT_OFFSET = 0x800
CTRL_OFFSET = 0x000

# Define shapes
BATCH = 1
SEQ_LEN = 4
HEADS = 2
HEAD_DIM = 16


def flatten_4d(tensor):
    return tensor.flatten()


# Generate random input tensors
q = np.random.randint(
    0, 10, (BATCH, SEQ_LEN, HEADS, HEAD_DIM), dtype=np.uint32)
k = np.random.randint(
    0, 10, (BATCH, SEQ_LEN, HEADS, HEAD_DIM), dtype=np.uint32)
v = np.random.randint(
    0, 10, (BATCH, SEQ_LEN, HEADS, HEAD_DIM), dtype=np.uint32)
print(f'this is Q: {q}')
print('\n')
print(f'this is K: {k}')
print('\n')
print(f'this is V: {v}')
print('\n')


# Flatten and write to IP
q_flat = flatten_4d(q)
k_flat = flatten_4d(k)
v_flat = flatten_4d(v)

for i in range(128):
    ip.write(Q_OFFSET + i*4, int(q_flat[i]))
    ip.write(K_OFFSET + i*4, int(k_flat[i]))
    ip.write(V_OFFSET + i*4, int(v_flat[i]))

# Start self-attention accelerator
ip.write(CTRL_OFFSET, 0x01)

# Wait for done
while (ip.read(CTRL_OFFSET) & 0x2) == 0:
    time.sleep(0.001)

# Read back output
out_flat = np.zeros(128, dtype=np.uint32)
for i in range(128):
    out_flat[i] = ip.read(OUT_OFFSET + i*4)

# Reshape output
out = out_flat.reshape((BATCH, SEQ_LEN, HEADS, HEAD_DIM))

print("Output from self-attention IP:\n", out)
