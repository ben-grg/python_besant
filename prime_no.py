'''
Finding prime numbers through operator overloading
by objects
'''
class TakeInput:
    def __init__(self,ui):
        self.user_input = ui

    def show(self):
        return self.user_input

    def __add__(self, other):
        return self.user_input + other

    def __mod__(self, other):
        return self.user_input % other

    def __floordiv__(self, other):
        return self.user_input // other

    def __gt__(self, other):
        return self.user_input > other

d = TakeInput(int(input("Enter data :\n")))

for i in range(2, d + 1 ):
    if d % i == 0 and d // i == 1:
        print(d.show()," is a prime number")
    elif d // i > 1 and d % i == 0:
        print(d.show()," is not a prime number")
        break
    else:
        pass

