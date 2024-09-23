
ancora = 'y'
while ancora == 'y':
    a = int(input('inserisci primo operando\n'))

    op = ''
    while op != '+' and op != '-' and op != '*' and op != '/':
        op = input('inserisci operazione\n')


    b = int(input('inserisci secondo operando\n'))

    if op == '+':
        print(a,op,b,'=',a+b)
    if op == '-':
        print(a,op,b,'=',a-b) 
    if op == '*':
        print(a,op,b,'=',a*b)
    if op == '/':
        print(a,op,b,'=',a/b)

    op_non_ok = op != '+' and op != '-' and op != '*' and op != '/'

    if op_non_ok:
        print('operzione non corretta')
    
    ancora = input('altra operazione? y/n ')




