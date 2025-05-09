from pynq import MMIO, allocate
import numpy as np


LAYER_NORM_ADDR = 0xA0090000  # base address for LayerNorm IP
INPUT_DMA_ADDR = 0xA00A0000  # DMA for input data
OUTPUT_DMA_ADDR = 0xA00B0000  # DMA for output data
LAYER_NORM_ADDR_OFFSET = 0x10  # Control register offset
A_SIZE = 24  # Systolic array size


layer_norm_ip = None
in_feature = None
out_feature = None

def ini_LayerNorm():
    global layer_norm_ip, in_feature, out_feature
    layer_norm_ip = MMIO(LAYER_NORM_ADDR, 0x10000)
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

def layer_norm(input_matrix, output_matrix):
    row, col = input_matrix[1]
    row_padded, col_padded = input_matrix[0].shape
    blocks_row = row_padded // A_SIZE
    blocks_col = col_padded // A_SIZE


    in_feature.write(0x10, input_matrix[0].device_address)  
    out_feature.write(0x10, output_matrix[0].device_address)  
    in_feature.write(0x00, 1)  
    out_feature.write(0x00, 1)  

    # Configure LayerNorm IP
    layer_norm_ip.write(0x00, 0)  
    layer_norm_ip.write(0x04, row_padded)  
    layer_norm_ip.write(0x08, col_padded) 
    layer_norm_ip.write(0x0C, blocks_row)  
    layer_norm_ip.write(0x14, blocks_col)  
    layer_norm_ip.write(LAYER_NORM_ADDR_OFFSET, 1)  

  
    while (out_feature.read(0x00) & 0x4) == 0:  
        pass
