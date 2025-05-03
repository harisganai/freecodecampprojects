import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 Numpy array
    arr = np.array(lst).reshape(3, 3)
    
    # Calculate statistics
    result = {
        'mean': [
            arr.mean(axis=0).tolist(),  # Mean of columns
            arr.mean(axis=1).tolist(),  # Mean of rows
            arr.mean().tolist()         # Mean of all elements
        ],
        'variance': [
            arr.var(axis=0).tolist(),   # Variance of columns
            arr.var(axis=1).tolist(),   # Variance of rows
            arr.var().tolist()          # Variance of all elements
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),   # Std of columns
            arr.std(axis=1).tolist(),   # Std of rows
            arr.std().tolist()          # Std of all elements
        ],
        'max': [
            arr.max(axis=0).tolist(),   # Max of columns
            arr.max(axis=1).tolist(),   # Max of rows
            arr.max().tolist()          # Max of all elements
        ],
        'min': [
            arr.min(axis=0).tolist(),   # Min of columns
            arr.min(axis=1).tolist(),   # Min of rows
            arr.min().tolist()          # Min of all elements
        ],
        'sum': [
            arr.sum(axis=0).tolist(),   # Sum of columns
            arr.sum(axis=1).tolist(),   # Sum of rows
            arr.sum().tolist()          # Sum of all elements
        ]
    }
    
    return result