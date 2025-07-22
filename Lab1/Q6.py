#A6
array1 = [20, 6, 2, 386]
array2 = [16, 3, 6, 289]
# Compute dot product
dot = 0
for i in range(len(array1)):
    dot += array1[i] * array2[i]

# Compute magnitudes
mag_array1 = sum([x*x for x in array1]) ** 0.5
mag_array2 = sum([x*x for x in array2]) ** 0.5

# Compute cosine similarity
cos_sim = dot / (mag_array1 * mag_array2) if mag_array1 != 0 and mag_array2 != 0 else 0

# Output
print("Version 1: Raw Vectors")
print("Cosine Similarity:", round(cos_sim, 4))