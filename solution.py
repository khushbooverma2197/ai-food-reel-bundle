import numpy as np
X = np.array([[1.0, 2.0, -1.0]])
W1 = np.array([
   [0.2, -0.1, 0.4, 0.3],
   [0.1, 0.3, -0.2, 0.05],
   [-0.3, 0.2, 0.1, -0.4]
])
b1 = np.array([[0.1, 0.0, -0.05, 0.2]])
W2 = np.array([
   [0.5],
   [-0.3],
   [0.2],
   [0.4]
])
b2 = np.array([[0.1]])

def relu(z):
   return np.maximum(0, z)

def forward_pass(X, W1, b1, W2, b2):
   z1 = X @ W1 + b1
   A1 = relu(z1)
   z2 = A1 @ W2 + b2
   return z1, A1, z2

z1, A1, z2 = forward_pass(X, W1, b1, W2, b2)
print(z1)
print(A1)
print(z2)
