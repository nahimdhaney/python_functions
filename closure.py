
# get Numbers
def make_repeater_of(stringToRepeat):
    def repeat(times):
        assert type(times) == int, "es necesario ingresar un numero"
        # newlist = [stringToRepeat for x in range(times)]
        return stringToRepeat * times
    return repeat

def make_division_by(n):
    # def division(x):
    #     return x/n       
    # return division
    # or using lambda
    return lambda x: x/n

# val = make_repeater_of("hola")
# print(val(5))

def run():
    rep_nahim = make_repeater_of("Nahim")
    print(rep_nahim(4))
    divisor = make_division_by(2)
    print(divisor(60))
    

if __name__ == '__main__':
    run()