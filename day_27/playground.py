def add(*args):
    return sum(args)

#print(add(1,2,3,4))

######################

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #print(kwargs["add"], kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

#calculate(2, add=3, multiply=5)    

######################

class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs["make"]
        self.model = kwargs.get("model") # в случае с get, не будет проблем при инициации объекта без передачи этого аргумента

my_car = Car(make="Nissan", model="Juke")
print(my_car.model)

