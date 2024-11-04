def wrap(f):
    def newf(*pars):
        print('decorazione')
        f(*pars)
    return newf

#stampa = wrap(stampa)
@wrap
def stampa(nome, cognome):
    print('ciao',nome,cognome)




stampa('marco','mamei')