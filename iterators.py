import time

class FiboIter():
    def __init__(self, *args, **kwargs):
        if 'max' in kwargs:
            self.max = kwargs.get("max")
        else:
            self.max = float("inf")
        if 'min' in kwargs:
            self.min = kwargs.get("min")

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self# siempre retornar el objeto en si mismo
    
    def __next__(self):
        if self.counter == 0:
            self.counter+=1
            return self.n1
        elif self.counter ==1:
            self.counter+=1
            return self.n2
        elif self.counter < self.max:
            self.counter+=1
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1,self.n2 = self.n2, self.aux #swapping
            return self.aux
        else:
            raise StopIteration
        

if __name__ == "__main__":
    fibo = FiboIter(max=5)
    fibo = iter(fibo)
    # for _ in range(5):
    #     element = next(fibo)
    #     print(element)
    
    for element in fibo:
        print(element)
        time.sleep(0.5)