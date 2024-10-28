def read_matrices(file_path):
    matrices = []
    with open(file_path, 'r') as file:
        matrix = []
        for line in file:
            line = line.strip()
            if line:  # If the line is not empty
                #row = list(map(int, line.split(',')))
                row = [int(x) for x in line.split(',')]
                matrix.append(row)
            else:  # Empty line indicates a new matrix
                if matrix:
                    matrices.append(matrix)
                    matrix = []
        if matrix:  # Add the last matrix if there is no trailing empty line
            matrices.append(matrix)
    return matrices


def sum(a,b): # a e b sono liste di liste di numeri
    c = [[0 for _ in r] for r in a]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

def dif(a,b): # a e b sono liste di liste di numeri
    c = [[0 for _ in r] for r in a]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] - b[i][j]
    return c

def prd(a,b): # a e b sono liste di liste di numeri
    c = [[0 for _ in r] for r in a]
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] * b[i][j]
    return c

print('*****')
print(__name__)
print('*****')

if __name__ == '__main__':
    c = sum([[1,2],[3,4]], [[1,2],[0,0]])
    print('-----------')
    print(c)