import random 
import time
import timeit

def generate(max):
    return [random.randint(1,500) for _ in range(max)]

def original(max):
    r = []
    for _ in range(max):
        r.append(random.randint(1,500))
    return r

parametro = 10_000_000
f_medir2 = lambda:original(parametro)
f_medir = lambda:generate(parametro)


tiempo2 =  timeit.timeit(f_medir2, number=1)
tiempo =  timeit.timeit(f_medir, number=1)

print(tiempo, tiempo2)



# b = timeit.timeit(original, number=1)
