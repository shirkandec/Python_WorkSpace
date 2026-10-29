# class book :
    # def __init__(self,t,p,pg,auth):
# # python is dynamically typed language so it does not support method overloading / or constructor overloading
# # & if we want to do it then we last update OR last calles function  OR method will be run 

# # abritory arguments are used for  known input number 



#         self.title=t
#         self.price=p
#         self.pages=pg
#         self.author=auth


# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# print(D.__mro__)





class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return A(self.value + other.value)

    def __sub__(self, other):
        return A(self.value - other.value)

    def __mul__(self, other):
        return A(self.value * other.value)

    def __truediv__(self, other):
        return A(self.value / other.value)

    def __floordiv__(self, other):
        return A(self.value // other.value)

    def __mod__(self, other):
        return A(self.value % other.value)

    def __pow__(self, other):
        return A(self.value ** other.value)

    def display(self):
        print(self.value)


a = A(20)
b = A(10)

c = a + b
c.display()

c = a - b
c.display()

c = a * b
c.display()

c = a / b
c.display()

c = a // b
c.display()

c = a % b
c.display()

c = a ** b
c.display()
