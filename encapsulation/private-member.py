# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = 1
        self.__c = 2

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

print(obj1.c)
# raise an AttributeError

obj2 = Derived()
# also raise an AtrributeError as
# private member of base class
# is called inside derived class
