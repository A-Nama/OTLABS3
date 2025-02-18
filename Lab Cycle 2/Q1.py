import numpy as np

def vogel_approximation_method(supply, demand, cost_matrix):
    supply = np.array(supply, dtype=int)
    demand = np.array(demand, dtype=int)
    cost_matrix = np.array(cost_matrix, dtype=int)
    
    n_rows, n_cols = cost_matrix.shape
    allocation = np.zeros((n_rows, n_cols), dtype=int)
    while np.any(supply>0) and np.any(demand>0):
        row_penalties = []
        col_penalties = []
        
        for i in range(n_rows):
            if supply[i]>0:
                row = [cost_matrix[i][j] for j in range(n_cols) if demand[j]>0]
                if len(row)>1:
                    penalties.append((i, -1, sorted(row)[:2]))
                elif len(row) == 1:
                    penalties.append((i, -1, [row[0], row[0]]))
                    
        for j in range(n_cols):
            if demand[j]>0:
                col = [cost_matrix[i][j] for i in range(n_rows) if supply[i]>0]
                if len(col)>1:
                    penalties.append((i, -1, sorted(col)[:2]))
                elif len(col) == 1:
                    penalties.append((i, -1, [col[0], col[0]]))
                    
        penalties = [(idx,axis,vals[1] - vals[0]) for idx ,axis, vals in penalties]
        max_penalty = max(penalties, key= lambda x : x[2])
        
        if max_penalty[1]==-1:
            row_idx = max_penalty[0]
            col_idx= np.argmin([cost_matrix[row_idx][j]if demand[j]>0 else float('inf') for j in range(n_cols)])
        else:
            
            