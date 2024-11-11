lst = [1, 2, 3, 4, 5]
result = [lst[i] - lst[-(i+1)] for i 
in range(len(lst)//2)]
print(result)