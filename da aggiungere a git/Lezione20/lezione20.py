
def ciao(name: str):

    return f'Ciao, {name}'

def salve(name: str):

    return f'Salve, {name}'

def saluta_bob(func):

    return func('Bob')

print(saluta_bob(ciao))
print(saluta_bob(salve))


#####


def parent():

    print('Sono in parent')

    def first_child():

        print('Sono in first_child')

    return first_child
    

print(parent())


####


def decorator(func):

    def wrapper(*args):
        import time

        start = time.time()

        func(*args)

        print(f"Time elapsed: {time.time() - start}")

    return wrapper


def ciao():

    print(f"Caio")

ciao = decorator(ciao)

ciao()

####

import time


class FileManager:
    
    def __init__(self, file_name: str, mode: str) -> None:
        
        self.file_name: str = file_name
        self.mode: str = mode
    
    
    def __enter__(self):
        
        self.file_wrapper = open(self.file_name, self.mode)
        
        return self.file_wrapper
    
    def __exit__(self, exc_type, exc_value, traceback):
        
        self.file_wrapper.close()
    
    
with FileManager(file_name="prova.txt", mode="w") as file:
    
    file.write("Ciao")
    
with open("prova.txt", "a") as file:
    
    file.write("Ciao")
    

class Timer:
    
    def __enter__(self):
        
        self.time = time.time()
        
    def __exit__(self, exc_type, exc_value, traceback):
        
        print(f"Time Elapsed: {time.time() - self.time}")
        
        return False


def ciao(name: str) -> str:
    
    print(f"Ciao, {name}")

def salve(name: str) -> str:
    
    print(f"Salve, {name}")

def saluta_bob(func) -> str:
    
    func("Bob")

print(saluta_bob(ciao))
print(saluta_bob(salve))

def parent():
    
    print("Sono in parent!")

    
    def first_child():
        
        print("Sono in First Child!")
    
    return first_child








def decorator(func):
    
    def wrapper(*args):
        import time
        
        start = time.time()
        
        func(*args)
        
        print(f"Time elapsed: {time.time() - start}")
        
    return wrapper

from merge import mergeSort


mergeSort = decorator(mergeSort)
import random
lista = [random.randint(0, 100000) for _ in range(100000)]
mergeSort(lista)

# import random

# lista = [random.randint(0, 100000) for _ in range(100000000)]

# with Timer():
    
#     mergeSort(lista)

# def bubble_sort_v2(x: list[int]):
#     # Ω(n) -> caso migliore quando la lista è già ordinata
#     # O(n^2) -> caso peggiore
#     ho_fatto_swap: bool = True
#     for i in range(len(x)):
#         for j in range(len(x) - i - 1):
#             if x[j] > x[j+1]:
#                 # swap(x[j], x[j+1])
#                 ho_fatto_swap = False
#                 temp: int = x[j]
#                 x[j] = x[j+1]
#                 x[j+1] = temp
#         if ho_fatto_swap:
#             break

# if __name__ == "__main__":
    
#     import random
#     import time
#     import matplotlib.pyplot as plt
    
#     merge_sort_times: list[float] = []
#     bubble_sort_times: list[float] = []
#     cases = [10, 50, 100, 250, 500, 1000, 1500, 2000, 5000, 10000, 20000]
#     for n in cases:
        
#         list_input: list[int] = [random.randint(0, 100000) for _ in range(n)]
        
#         start = time.time()    
#         result: list[int] = mergeSort(list_input=list_input)
#         end = time.time()
        
#         merge_sort_times.append(end-start)
            
#         start = time.time()
#         result: list[int] = bubble_sort_v2(x=list_input)
#         end = time.time()
        
#         bubble_sort_times.append(end-start)
        
#     print(f"MERGE: {merge_sort_times}\nBUBBLE: {bubble_sort_times}")
#     plt.plot(cases, merge_sort_times, label="Merge")
#     plt.plot(cases, bubble_sort_times, label="Bubble")
#     plt.yscale("log")
#     plt.xscale("log")
#     plt.legend()
#     plt.show()
# class Esempio:
    
#     def __init__(self, name) -> None:
        
#         self.__name = self.__checkName(name)
#         self.__attr_1 = None
#         self._attr_1 = None
#         self.attr_1 = None
        
        
#     def __checkName(self, name: str):
        
#         #
        
        
#         return name.capitalize()      
        
#     def setName(self, name: str):
                
#         self.attr_1 = self.__checkName(name)
        


# es = Esempio()

# es.attr_1 = "fLAvIo"

# "Flavio"



# # reader = open("files/esempio.txt")
# # print(reader)

# # reader.close()

# # with open(f"files/esempio.txt") as f:
    
# #     print()


# # reader = open("files/esempio.txt")
    
# # try:
    
# #     reader.readline()
# #     print("Sono nella try")
# #     raise Exception("Eccezione!")
    
# # except Exception:
    
# #     print("Sono nella except")
    
# # finally:
    
# #     print(reader)

# #     reader.close()    
        
# #     print("sono nella finally")
    
 
# with open("files/esempio.txt", "a") as reader:
#     l = [f"Ciao sono Flavio\n", f"Ciao sono Maria\n", f"Ciao sono Luca\n"]
#     reader.writelines(l)
    
 
    
# # with open("files/esempio.txt") as reader:
    
# #     line = reader.readline()
# #     line_counter = 0
# #     while line != '':
        
# #         print(f"{line} - number: {line_counter}")
# #         line = reader.readline()
# #         line_counter += 1
    
    
    
# class VotoTroppoBassoError(Exception):
    
#     # def __init__(self, *args: object) -> None:
#     #     super().__init__(*args)
#     pass


# class VotoBruttissimo(VotoTroppoBassoError):
    
#     pass
  
    
# # class ContextManager:
    
# #     def __enter__(self):
        
# #         print("Ciao sono nell'enter")
        
# #         return self
    
# #     def __exit__(self, exc_type, exc_value, traceback):
        
# #         if exc_type is not None:
            
# #             print("Eccezione")
            
# #         return False
        

# try:
    
#     print("Sono nel try")
#     raise VotoTroppoBassoError("Prova")
            
# except ZeroDivisionError as e:
        
#     print("Sono nel ZeroDiv")
    
# except ValueError as e:
    
#     print("Sono nel ValueError")

# except ImportError as e:
    
#     print(f"Warning: {e}")
    
# except VotoTroppoBassoError as e:
    
#     print(f"Warning: {e}")
    
# else:
    
#     print("Sono nell'else")
          
# finally:
    
#     print("Sono nel finally")
    
    
# import time
# from contextlib import contextmanager

# @contextmanager
# def timer():
    
#     start = time.time()
#     print("__enter__")
    
#     yield "Ciao"
    
#     print("__exit__")
#     end = time.time()
#     elapsed_time = end -start
    
#     print(f"time elapsed: {elapsed_time}")
    
    
# if __name__ == "__main__":
    
    
#     with timer() as t:
#         print(t)
#         print("with")
#         time.sleep(1)
        
  
####


# GESTIONALE PAGAMENTO


class Pagamento:

    def __init__(self):
        self._importo = None


    def get(self):

        return self._importo


    def set(self, importo: float):
        self._importo = importo

    
    def dettagliPagamento(self):

        print(f"Importo del pagamento: {self._importo}")


class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__(self._importo)


    def dettagliPagamento(self):

        print(f"{self._importo} da pagare in contanti:")


    def inPezziDa(self):

        resto = self._importo
        soldi: list[float] = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]

        for x in soldi:
            quantità = resto / soldi

            if quantità > 0:
                
            

    







class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, nome_titolare_carta: str, data_scadenza: str, numero_carta: int):
        super().__init__(self._importo)
        self.nome_titolare_carta: str = nome_titolare_carta
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta


