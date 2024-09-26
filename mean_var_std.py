import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3, 3)

    mean_axs1 = np.mean(matrix, axis=0).tolist()
    mean_axs2 = np.mean(matrix, axis=1).tolist()
    mean_flattened = np.mean(matrix).tolist()

    var_axs1 = np.var(matrix, axis=0).tolist()
    var_axs2 = np.var(matrix, axis=1).tolist()
    var_flattened = np.var(matrix).tolist()

    std_axs1 = np.std(matrix, axis=0).tolist()
    std_axs2 = np.std(matrix, axis=1).tolist()
    std_flattened = np.std(matrix).tolist()

    max_axs1 = np.max(matrix, axis=0).tolist()
    max_axs2 = np.max(matrix, axis=1).tolist()
    max_flattened = np.max(matrix).tolist()

    min_axs1 = np.min(matrix, axis=0).tolist()
    min_axs2 = np.min(matrix, axis=1).tolist()
    min_flattened = np.min(matrix).tolist()

    sum_axs1 = np.sum(matrix, axis=0).tolist()
    sum_axs2 = np.sum(matrix, axis=1).tolist()
    sum_flattened = np.sum(matrix).tolist()

    calculations = {
        'mean': [mean_axs1, mean_axs2, mean_flattened],
        'variance': [var_axs1, var_axs2, var_flattened],
        'standard deviation': [std_axs1, std_axs2, std_flattened],
        'max': [max_axs1, max_axs2, max_flattened],
        'min': [min_axs1, min_axs2, min_flattened],
        'sum': [sum_axs1, sum_axs2, sum_flattened]
    }

    return calculations