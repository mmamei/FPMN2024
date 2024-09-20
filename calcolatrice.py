a = int(input('inserisci primo operando\n'))
op = input('inserisci operazione\n')
b = int(input('inserisci secondo operando\n'))

if op == '+':
    print(a,op,b,'=',a+b)
elif op == '-':
    print(a,op,b,'=',a-b) 
elif op == '*':
    print(a,op,b,'=',a*b)
elif op == '/':
    print(a,op,b,'=',a/b)
else:
    print('operzione non corretta')




