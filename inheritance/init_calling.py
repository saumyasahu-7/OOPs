class A:
    def __init__(self):
        print("A's init called")

class B(A):
    def __init__(self):
        print("B's init called")
        super().__init__()

class C(A):
    def __init__(self):
        print("C's init called")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D's init called")
        super().__init__()

# Creating an instance of D
d = D()

# Checking the MRO of D
print(D.__mro__)
