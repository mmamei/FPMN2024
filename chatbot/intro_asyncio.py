'''

# https://realpython.com/python-concurrency/
# https://realpython.com/async-io-python

Programmazione Parallela o Concorrente:

Il Parallelismo consiste nell'eseguire più operazioni contemporaneamente. 

Il multiprocessing è un mezzo per realizzare il parallelismo
comporta la distribuzione dei compiti tra le CPU o Core di un computer. 
Il multiprocessing è particolarmente adatto per attività che richiedono un uso 
intensivo della CPU
---> libreria multiprocessing in python

La concorrenza (concurrency) è un termine leggermente più ampio rispetto al parallelismo. 
Indica che più attività hanno la capacità di essere eseguite in modo sovrapposto. 
Non è detto che debbano eseguire su CPU diverse contemporanemante. 
Una sola CPU può eseguire in modo alternante (iterleaving) diversi task che sembrano
procedere in parallelo.
Ad esempio voglio fare qualcosa mentre aspetto un'operazione bloccante

Il threading è un modello di esecuzione concorrente in cui più thread 
si alternano nell'esecuzione di compiti. Il sistema operativo supporta i thread e il
"preemptive multitasking", sospendere un thread per eseguirne un altro.
---> libreria threading in python

Asynchronous tasks è un modello di esecuzione concorrente basato su un singolo thread.
Il sistema operativo non è coinvolto e l'alternanza tra task (i.e., funziioni) 
si basa sul "cooperative multitasking".
Sono i task stessi a indicare quando possono essere interrotte.
----> libreria asyncio

'''
'''

import time

def count():
    print("One")
    time.sleep(5)
    print("Two")

def main():
    for _ in range(3):
        count()

main()

'''
import asyncio

async def count():
    print("One")
    await asyncio.sleep(5)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())
