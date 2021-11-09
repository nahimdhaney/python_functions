from datetime import datetime


def execution_time(func):
    def wrapper(*args,**kargs):
        inicial_time = datetime.now()
        func(*args,**kargs)
        final_time = datetime.now()
        time_elapsed =  final_time- inicial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,10000000):
        pass

random_func()


@execution_time
# def suma(a: int,b : int) -> int:
def suma(a,b):
    print(f'sumando {a} y {b}')
    # print(a+b)
    return a + b

valor_creado = suma(2,4)
print(valor_creado)
