from pynq import MMIO, allocate
import numpy as np

# Constants
SOFTMAX_ADDR = 0xA0030000  # base address for Softmax IP
INPUT_DMA_ADDR = 0xA0040000  # DMA for input data
OUTPUT_DMA_ADDR = 0xA0050000  # DMA for output data
SOFTMAX_ADDR_OFFSET = 0x10  # Control register offset (to start operation)
A_SIZE = 24  # Systolic array size (same as MM.py)

# Global variables
softmax_ip = None
in_feature = None
out_feature = None

def ini_Softmax():
    # Initialize the Softmax IP core and DMA controllers.
    global softmax_ip, in_feature, out_feature
    softmax_ip = MMIO(SOFTMAX_ADDR, 0x10000)
    in_feature = MMIO(INPUT_DMA_ADDR, 0x10000)
    out_feature = MMIO(OUTPUT_DMA_ADDR, 0x10000)

def vec_create(shape):
    # Create a matrix with padding to match A_SIZE
    row, col = shape
    row_padded = row + (A_SIZE - row % A_SIZE) if row % A_SIZE != 0 else row
    col_padded = col + (A_SIZE - col % A_SIZE) if col % A_SIZE != 0 else col
    buffer = allocate(shape=(row_padded, col_padded), dtype=np.int8)
    return [buffer, np.array([row, col])]

def vec_setValue(vec, ndarray):
    # Set the values of the matrix.
    vec[0][:ndarray.shape[0], :ndarray.shape[1]] = ndarray

def vec_getNdarray(vec):
    # Get the matrix as a NumPy array.
    shape = vec[1]
    return vec[0][:shape[0], :shape[1]]

def softmax(input_matrix, output_matrix):
    # Perform softmax operation on the input matrix.
    # Get padded dimensions
    row, col = input_matrix[1]
    row_padded, col_padded = input_matrix[0].shape
    blocks_row = row_padded // A_SIZE
    blocks_col = col_padded // A_SIZE

    # DMA transfers
    in_feature.write(0x10, input_matrix[0].device_address)  # Input buffer address
    out_feature.write(0x10, output_matrix[0].device_address)  # Output buffer address
    in_feature.write(0x00, 1)  # Start input DMA
    out_feature.write(0x00, 1)  # Start output DMA

    # Configure Softmax IP
    softmax_ip.write(0x00, 0)  # Reset
    softmax_ip.write(0x04, row_padded)  # Number of rows
    softmax_ip.write(0x08, blocks_row)  # Number of row blocks
    softmax_ip.write(0x0C, blocks_col)  # Number of column blocks
    softmax_ip.write(SOFTMAX_ADDR_OFFSET, 1)  # Start operation

    # Wait for completion
    while (out_feature.read(0x00) & 0x4) == 0:  # Check DMA done bit
        pass
