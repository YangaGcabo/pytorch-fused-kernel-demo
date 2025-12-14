import torch

def fused_operation(x):
    return torch.relu(x + 1) * 2

x = torch.randn(5)
y = fused_operation(x)

print("Input:", x)
print("Output:", y)
