import time

def fibo_gen(limit=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        elif not limit or  counter <limit :
            counter+=1
            aux = n1 + n2
            n1,n2 = n2, aux #swapping
            yield aux
        else:
            break

if __name__ == "__main__":
    fibo = fibo_gen()
    for element in fibo:
        print(element)
        time.sleep(0.5)        
