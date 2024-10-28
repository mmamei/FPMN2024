'''
scrivere un programma python
dato il file dati.txt che contiene una lista di matrici.
Memorizzare le matrici in una lista di liste di liste di numeri
'''

def read_matrices(file_path):
    matrices = []
    with open(file_path, 'r') as file:
        matrix = []
        for line in file:
            line = line.strip()
            if line:  # If the line is not empty
                row = list(map(int, line.split(',')))
                matrix.append(row)
            else:  # Empty line indicates a new matrix
                if matrix:
                    matrices.append(matrix)
                    matrix = []
        if matrix:  # Add the last matrix if there is no trailing empty line
            matrices.append(matrix)
    return matrices

# Usage example
file_path = '/mnt/data/dati.txt'
matrices = read_matrices(file_path)
print(matrices)
