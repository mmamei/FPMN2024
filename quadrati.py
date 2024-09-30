N = 7
for i in range(N):
    for j in range(N):
        if i == j or j == N - 1 - i:
            print('*',end= '  ')
        else:
            print('.',end= '  ')
    print('')