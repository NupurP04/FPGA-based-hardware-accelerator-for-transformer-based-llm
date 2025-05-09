from pynq import Overlay
from pynq import MMIO
import numpy as np
import time

# Load the bitstream
overlay = Overlay("llm.bit")
ip_base_addr = 0x43C00000
ip_range = 0x1000  # 4KB mapped range is usually enough

# MMIO interface to your custom IP
ip = MMIO(ip_base_addr, ip_range)

# Address offsets from HLS-generated control interface
Q_OFFSET = 0x200
K_OFFSET = 0x400
V_OFFSET = 0x600
OUT_OFFSET = 0x800
CTRL_OFFSET = 0x000

# Sample data (can be real numbers packed as uint32 via view())
q = np.random.randint(0, 100, 128, dtype=np.uint32)
k = np.random.randint(0, 100, 128, dtype=np.uint32)
v = np.random.randint(0, 100, 128, dtype=np.uint32)

# Write input arrays to memory-mapped registers
for i in range(128):
    ip.write(Q_OFFSET + i*4, int(q[i]))
    ip.write(K_OFFSET + i*4, int(k[i]))
    ip.write(V_OFFSET + i*4, int(v[i]))

# Start the IP core
ip.write(CTRL_OFFSET, 0x01)  # ap_start = 1

# Wait for ap_done (bit 1 in control register becomes 1)
while (ip.read(CTRL_OFFSET) & 0x2) == 0:
    time.sleep(0.001)

# Read the result
out = np.zeros(128, dtype=np.uint32)
for i in range(128):
    out[i] = ip.read(OUT_OFFSET + i*4)

# Display result
print("Output from self-attention IP:\n", out)
