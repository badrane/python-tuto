#!/usr/bin/env python

class FirstClass: # Define a class object
    def setdata(self, value): # Define class's methods
        self.data = value # self is the instance
    def display(self):
        print(self.data) # self.data: per instance


x = FirstClass() # Make two instances
y = FirstClass() # Each is a new namespace

x.setdata("Valeur") # Call methods: self is x
y.setdata(3.14159) # Runs: FirstClass.setdata(y, 3.14159)


x.display() # self.data differs in each instance
y.display() # Runs: FirstClass.display(y)

x.data= "Thomas"
x.display()

# ---------- add a class variable dynamically
x.othername = 'Test'
print(dir(x))

#------------- add method dynamically
import types

class A():
    pass

def patch_me(target):
    def method(target,x):
        print("x=",x)
        print("called from", target)
    target.method = types.MethodType(method,target)

a = A()
print(a)
patch_me(a)
a.method(5)

patch_me(A)
A.method(6)

#---------------------- Heritage

class SecondClass(FirstClass): # Inherits setdata
    def display(self): # Changes display
        print('Current value = "%s"' % self.data)

z = SecondClass()
z.setdata(42) # Finds setdata in FirstClass
z.display()


class ThirdClass(SecondClass): # Inherit from SecondClass
    def __init__(self, value): # On "ThirdClass(value)"
        self.data = value
    def __add__(self, other): # On "self + other"
        return ThirdClass(self.data + other)
    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data
    def mul(self, other): # In-place change: named
        self.data *= other



a = ThirdClass('abc') # __init__ called
a.display() # Inherited method called
print(a) # __str__: returns display string

b = a + 'xyz' # __add__: makes a new instance
b.display() # b has all ThirdClass methods
print(b) # __str__: returns display string

a.mul(3) # mul: changes instance in place
print(a)


#---- class attribute et instance attribute
class MixedNames: # Define class
    data = 'spam' # Assign class attr
    def __init__(self, value): # Assign method name
        self.data = value # Assign instance attr
    def display(self):
        print(self.data, MixedNames.data) # Instance attr, class attr

x = MixedNames(1) # Make two instance objects
y = MixedNames(2) # Each has its own data
x.display(); y.display()