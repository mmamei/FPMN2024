def fatt(n):
    if n == 1:
        return 1
    else:
        return n*fatt(n-1)
    
print(fatt(4))
