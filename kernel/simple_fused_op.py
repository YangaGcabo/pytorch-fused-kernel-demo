import torch

def fused_add_relu(x, y):
    """
    Simple fused operation: add + ReLU.
    Demonstrates understanding of operator fusion.
    """
    return torch.relu(x + y)
