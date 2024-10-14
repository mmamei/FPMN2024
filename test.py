
a = {
    'marco':[1,200,3,4],
    'anna':[6],
    'luca':[6]
}

b = sorted(a.items(), key=lambda x:sum(x[1])/len(x[1]), reverse=True)
print(b)



