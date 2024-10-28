'''
scrivere un programma python
dato il file dati.txt che contiene una lista di matrici.
Memorizzare le matrici in una lista di liste di liste di numeri
'''

from matop import read_matrices,sum,dif,prd

if __name__ == '__main__':
    # Usage example
    file_path = 'esame2/dati.txt'
    matrices = read_matrices(file_path)
    #print(matrices)
    a = matrices[0]
    b = matrices[1]
    c = matrices[2]

    # (a+b)*(c-b)
    
    r = prd(sum(a,b),dif(c,b))
    print(r)