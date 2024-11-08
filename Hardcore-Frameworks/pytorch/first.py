import torch

print(f"Hello, You are using torch version : {torch.__version__}\n")

### Introduce me tensors please!!!
# Scalar Tensors?

# fmt: off
# Date
scaler = torch.tensor(1)
print(f"Dimension of Scalar : {scaler.ndim}")
print(f"Shape of Scaler  : {scaler.shape}")
print(f"Size of Scaler  :  {scaler.size()}\n")

# Date of Birth
vector = torch.tensor(
    [1, 1, 1997]
)
print(f"Dimension of Vector : {vector.ndim}")
print(f"Shape of Vector  : {vector.shape}")
print(f"Size of Vector  :  {vector.size()}\n")

# Date of Birth of one family
matrix = torch.tensor(
    [
        [1, 1, 1997], 
        [1, 3, 2001], 
        [1, 6, 1977], 
        [1, 9, 1987]
    ]
)
print(f"Dimension of Matrix : {matrix.ndim}")
print(f"Shape of Matrix  : {matrix.shape}")
print(f"Size of Matrix  :  {matrix.size()}\n")

# Date of Birth of multiple families
tensor = torch.tensor(
    [
        [
            [1, 1, 1997], 
            [1, 3, 2001], 
            [1, 6, 1977], 
            [1, 9, 1987]
        ],
        [
            [2, 1, 1997], 
            [2, 3, 2001], 
            [2, 6, 1977], 
            [2, 9, 1987]
        ],            
        
    ]
)
print(f"Dimension of Tensor : {tensor.ndim}")
print(f"Shape of Tensor  : {tensor.shape}")
print(f"Size of Tensor  :  {tensor.size()}\n")

# fmt: on
