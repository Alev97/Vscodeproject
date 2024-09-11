
def decorator(func):


    def wrapper(*args):
        import time

        start = time.time()

        func(*args)

        print(f"Time elapsed: {time.time() - start}")


    return wrapper

'''
@Analisi.tempo
def area_cerchio(raggio: float):

    return raggio * raggio * 3.14

area_cerchio(1)
'''

####


def generatore():

    yield'A'
    yield'B'
    yield'C'

prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))

####

from contextlib import contextmanager

@contextmanager
def context_manager_decorator(*args):
    import time

    start_time: float = time.time()

    yield

    end_time: float = time.time()
    elapsed_time = end_time - start_time

    print(f'{elapsed_time}')


@context_manager_decorator
def area_cerchio(raggio: float):

    return raggio * raggio * 3.14

area_cerchio(1)