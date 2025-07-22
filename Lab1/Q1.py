# A1
import numpy as np

B= np.array([[20, 6, 2],[16, 3, 6],[27, 6, 2],[19, 1, 2],[24, 4, 2],[22, 1, 5],[15, 4, 2],[18, 4, 2],[21, 1, 4],[16, 2, 4]])
D = np.array([[386],[289],[393],[110],[280],[167],[271],[274],[148],[198]])
column = B.shape[1]
rows = D.shape[0]

_, singular_vals, _ = np.linalg.svd(D)
matrix_rank = sum(val > 1e-10 for val in singular_vals)

pseudo_inv = np.linalg.pinv(B)
costs = pseudo_inv @ D

print("RESULTS:")
print(f"Dimensionality of vector space : {column}")
print(f"Number of vectors              : {rows}")
print(f"Rank of Matrix A               : {matrix_rank}")
print("\nEstimated cost of each product:")
print(f"Cost of 1 Candy       : Rs {costs[0][0]:.2f}")
print(f"Cost of 1 Kg Mango    : Rs {costs[1][0]:.2f}")
print(f"Cost of 1 Milk Packet : Rs {costs[2][0]:.2f}")