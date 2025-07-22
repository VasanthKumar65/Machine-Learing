#A5
import numpy as np

# Binary Vectors for Jaccard & SMC
array1 = np.array([1, 0, 1, 1, 0, 1])
array2= np.array([1, 1, 1, 0, 0, 1])

# --- Jaccard Similarity ---
intersection = np.sum((array1 & array2))
union = np.sum((array1 | array2))
jaccard = intersection / union

# --- Simple Matching Coefficient (SMC) ---
matches = np.sum(array1 == array2)
smc = matches / len(array1)

print("---- Binary Similarity ----")
print(f"Jaccard Similarity      : {jaccard:.2f}")
print(f"Simple Matching Coef.   : {smc:.2f}")

# A5
C0 = [20, 6, 2, 386]
C1 = [16, 3, 6, 289]

# Fixed thresholds for binarization
thresholds = [18, 4, 3, 300]  # chosen manually based on general range

binary_C0 = []
binary_C1 = []

for i in range(len(C0)):
    binary_C0.append(1 if C0[i] > thresholds[i] else 0)
    binary_C1.append(1 if C1[i] > thresholds[i] else 0)

# Compare binary vectors
f11 = f10 = f01 = f00 = 0
for i in range(len(binary_C1)):
    if binary_C0[i] == 1 and binary_C1[i] == 1:
        f11 += 1
    elif binary_C0[i] == 1 and binary_C1[i] == 0:
        f10 += 1
    elif binary_C0[i] == 0 and binary_C1[i] == 1:
        f01 += 1
    else:
        f00 += 1

jc = f11 / (f11 + f10 + f01) if (f11 + f10 + f01) else 0
smc = (f11 + f00) / (f11 + f10 + f01 + f00) if (f11 + f10 + f01 + f00) else 0

print("Binary C0:", binary_C0)
print("Binary C1:", binary_C1)
print("JC:", round(jc, 4), "SMC:", round(smc, 4))