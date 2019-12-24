import numpy as np



def NormalMode(k, m):
    matrix = np.array([[2, -1, 0], [-1, 2, 1], [0, -1, 2]]) ;matrix = matrix * (k/m)
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    return print(eigenvalues), print(eigenvectors)
    


NormalMode(1, 1)