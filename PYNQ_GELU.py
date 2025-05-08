from pynq import MMIO, allocate
import numpy as np

GELU_ADDR = 0xA0020000  # base address for GELU IP
INPUT_DMA_ADDR = 0xA0030000  # DMA for input data
OUTPUT_DMA_ADDR = 0xA0040000  # DMA for output data
GELU_ADDR_OFFSET = 0x10  # Control register offset
A_SIZE = 24  # Systolic array size


gelu_ip = None
in_feature = None
out_feature = None

def ini_GELU():
    global gelu_ip, in_feature, out_feature
    gelu_ip = MMIO(GELU_ADDR, 0x10000)
    in_feature = MMIO(INPUT_DMA_ADDR, 0x10000)
    out_feature = MMIO(OUTPUT_DMA_ADDR, 0x10000)

def vec_create(shape):
    row, col = shape
    row_padded = row + (A_SIZE - row % A_SIZE) if row % A_SIZE != 0 else row
    col_padded = col + (A_SIZE - col % A_SIZE) if col % A_SIZE != 0 else col
    buffer = allocate(shape=(row_padded, col_padded), dtype=np.int8)
    return [buffer, np.array([row, col])]

def vec_setValue(vec, ndarray):
    vec[0][:ndarray.shape[0], :ndarray.shape[1]] = ndarray

def vec_getNdarray(vec):
    shape = vec[1]
    return vec[0][:shape[0], :shape[1]]

def gelu(input_matrix, output_matrix):
    row, col = input_matrix[1]
    row_padded, col_padded = input_matrix[0].shape
    total_elements = row_padded * col_padded

    # DMA transfers
    in_feature.write(0x10, input_matrix[0].device_address)  # Input buffer address
    out_feature.write(0x10, output_matrix[0].device_address)  # Output buffer address
    in_feature.write(0x00, 1)  # Start input DMA
    out_feature.write(0x00, 1)  # Start output DMA

    # Configure GELU IP
    gelu_ip.write(0x00, 0)  # Reset
    gelu_ip.write(0x04, total_elements)  # Total number of elements
    gelu_ip.write(GELU_ADDR_OFFSET, 1)  # Start operation

    while (out_feature.read(0x00) & 0x4) == 0:  # Check DMA done bit
        pass
