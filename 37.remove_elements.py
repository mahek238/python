def remove_indices(lst): 
    indices = [0, 2, 3, 5] 
    return [item for i, item in enumerate(lst) if i not in indices] 
print(remove_indices([10, 20, 30, 40, 50, 60, 70]))