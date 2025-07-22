#A7
import numpy as np

# Hardcoded 20 binary observation vectors (6 binary features each)
dataset = [
    [1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0],
]

n = len(dataset)
jc_matrix = np.zeros((n, n))
smc_matrix = np.zeros((n, n))
cos_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        vec1 = np.array(dataset[i])
        vec2 = np.array(dataset[j])

        f11 = np.sum((vec1 == 1) & (vec2 == 1))
        f10 = np.sum((vec1 == 1) & (vec2 == 0))
        f01 = np.sum((vec1 == 0) & (vec2 == 1))
        f00 = np.sum((vec1 == 0) & (vec2 == 0))

        jc = f11 / (f11 + f10 + f01) if (f11 + f10 + f01) else 0
        smc = (f11 + f00) / (f11 + f10 + f01 + f00) if (f11 + f10 + f01 + f00) else 0

        dot = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        cos = dot / (norm1 * norm2) if (norm1 * norm2) else 0

        jc_matrix[i][j] = round(jc, 3)
        smc_matrix[i][j] = round(smc, 3)
        cos_matrix[i][j] = round(cos, 3)

# --- Print Result Matrices ---

print("\n=== Jaccard Coefficient Matrix ===")
for row in jc_matrix:
    print(row.tolist())

print("\n=== Simple Matching Coefficient Matrix ===")
for row in smc_matrix:
    print(row.tolist())

print("\n=== Cosine Similarity Matrix ===")
for row in cos_matrix:
    print(row.tolist())