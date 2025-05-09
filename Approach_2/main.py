from pynq import Overlay, MMIO
import numpy as np
import time

# Constants
SEQ_LEN = 4
EMBED_DIM = 32
HEADS = 2
HEAD_DIM = EMBED_DIM // HEADS
VOCAB_SIZE = 265

# Offsets for IP
Q_OFFSET = 0x200
K_OFFSET = 0x400
V_OFFSET = 0x600
OUT_OFFSET = 0x800
CTRL_OFFSET = 0x000

# Load FPGA bitstream and MMIO
overlay = Overlay("shreeya.bit")
ip = MMIO(0x43C00000, 0x1000)

# ---------------- FPGA Self-Attention ----------------


def run_self_attention(q, k, v):
    q_u32 = q.view(np.uint32)
    k_u32 = k.view(np.uint32)
    v_u32 = v.view(np.uint32)

    for i in range(128):
        ip.write(Q_OFFSET + i * 4, int(q_u32[i]))
        ip.write(K_OFFSET + i * 4, int(k_u32[i]))
        ip.write(V_OFFSET + i * 4, int(v_u32[i]))

    ip.write(CTRL_OFFSET, 0x01)
    while (ip.read(CTRL_OFFSET) & 0x2) == 0:
        time.sleep(0.001)

    out_u32 = np.zeros(128, dtype=np.uint32)
    for i in range(128):
        out_u32[i] = ip.read(OUT_OFFSET + i * 4)

    return out_u32.view(np.float32)

# ----------------- Utilities ------------------------


def load_vocab(filename):
    vocab = {}
    with open(filename) as f:
        for line in f:
            word, id_ = line.strip().split()
            vocab[word] = int(id_)
    return vocab


def tokens_from_words(words, vocab):
    return [vocab.get(w, 0) for w in words]


def word_from_token(id_, vocab):
    for word, idx in vocab.items():
        if idx == id_:
            return word
    return "<UNK>"


def load_weights(filename, shape):
    return np.fromfile(filename, dtype=np.float32).reshape(shape)


def dot(a, b):
    return float(np.dot(a, b))

# ----------------- Inference ------------------------


def forward(input_tokens, embedding, W_q, W_k, W_v, W_o, b_o):
    input_embed = embedding[input_tokens]  # shape [SEQ_LEN, EMBED_DIM]

    # Project to Q, K, V
    Q = np.zeros((SEQ_LEN, HEADS, HEAD_DIM), dtype=np.float32)
    K = np.zeros((SEQ_LEN, HEADS, HEAD_DIM), dtype=np.float32)
    V = np.zeros((SEQ_LEN, HEADS, HEAD_DIM), dtype=np.float32)

    for t in range(SEQ_LEN):
        for h in range(HEADS):
            for d in range(HEAD_DIM):
                Q[t][h][d] = np.dot(input_embed[t], W_q[h * HEAD_DIM + d])
                K[t][h][d] = np.dot(input_embed[t], W_k[h * HEAD_DIM + d])
                V[t][h][d] = np.dot(input_embed[t], W_v[h * HEAD_DIM + d])

    # Flatten and run FPGA
    Q_flat = Q.flatten()
    K_flat = K.flatten()
    V_flat = V.flatten()
    context_flat = run_self_attention(Q_flat, K_flat, V_flat)
    context = context_flat.reshape((SEQ_LEN, HEADS, HEAD_DIM))

    # Concatenate heads for last token
    final_vec = np.concatenate(context[-1])  # shape [EMBED_DIM]

    # Output projection
    proj = np.dot(W_o, final_vec) + b_o

    # Softmax is skipped — argmax for prediction
    scores = embedding @ proj  # shape [VOCAB_SIZE]
    return int(np.argmax(scores))

# ------------------ Main ----------------------------


if __name__ == "__main__":
    vocab = load_vocab("vocab.txt")
    # words = ["hello", "how", "are", "you"]
    words = ["Jackson", "saw", "and", "felt"]
    tokens = tokens_from_words(words, vocab)

    # embedding = load_weights("embedding.bin", (VOCAB_SIZE, EMBED_DIM))
    embedding = np.fromfile("embedding.bin", dtype=np.float32)[
        :8448].reshape((264, 32))
    W_q = load_weights("W_q.bin", (EMBED_DIM, EMBED_DIM))
    W_k = load_weights("W_k.bin", (EMBED_DIM, EMBED_DIM))
    W_v = load_weights("W_v.bin", (EMBED_DIM, EMBED_DIM))
    W_o = load_weights("W_o.bin", (EMBED_DIM, EMBED_DIM))
    b_o = load_weights("b_o.bin", (EMBED_DIM,))

    print("Input:", " ".join(words))
    print("Predicted next 3 words:")

    for _ in range(3):
        pred_id = forward(tokens, embedding, W_q, W_k, W_v, W_o, b_o)
        pred_word = word_from_token(pred_id, vocab)
        print(pred_word, end=' ')
        tokens = tokens[1:] + [pred_id]

print()
