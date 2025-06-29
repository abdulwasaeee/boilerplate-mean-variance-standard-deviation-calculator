import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(lst).reshape(3, 3)

    d = {
        'mean': [list(np.mean(a, axis=0)), list(np.mean(a, axis=1)), float(np.mean(a))],
        'variance': [list(np.var(a, axis=0)), list(np.var(a, axis=1)), float(np.var(a))],
        'standard deviation': [list(np.std(a, axis=0)), list(np.std(a, axis=1)), float(np.std(a))],
        'max': [list(np.max(a, axis=0)), list(np.max(a, axis=1)), float(np.max(a))],
        'min': [list(np.min(a, axis=0)), list(np.min(a, axis=1)), float(np.min(a))],
        'sum': [list(np.sum(a, axis=0)), list(np.sum(a, axis=1)), int(np.sum(a))]
    }

    return d
