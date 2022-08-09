'''
Polymorphism with Inheritance:
*****************************
2 methods with same name with same number of parmeters or arguments 
it is method overriding

the child classes in Python also inherit methods and attributes from the 
parent class. We can redefine certain methods and attributes specifically to 
fit the child class, which is known as Method Overriding.

Polymorphism allows us to access these overridden methods and attributes that 
have the same name as the parent class.

############
we can see that the methods such as __str__(), which have not been overridden 
in the child classes, are used from the parent class.

Due to polymorphism, the Python interpreter automatically recognizes that the 
fact() method for object a(Square class) is overridden. So, it uses the one 
defined in the child class.

On the other hand, since the fact() method for object b isn't overridden, 
it is used from the Parent Shape class.
'''
from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
########################################
Note: Method Overloading, a way to create multiple methods with the same name 
but different arguments, is not possible in Python
#################Polymorphism with Inheritance########################
class Bird:
  def intro(self):
    print("There are many types of birds.")
      
  def flight(self):
    print("Most of the birds can fly but some cannot.")
    
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
      
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
      
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()
############Polymorphism with a Function and objects:##########################
'''
It is also possible to create a function that can take any object, allowing for 
polymorphism. In this example, let’s create a function called “func()” 
which will take an object which we will name “obj”. Though we are using the 
name ‘obj’, any instantiated object will be able to be called into this function. 
Next, lets give the function something to do that uses the ‘obj’ object we passed 
to it. In this case lets call the three methods, viz., capital(), language() 
and type(), each of which is defined in the two classes ‘India’ and ‘USA’. Next, 
let’s create instantiations of both the ‘India’ and ‘USA’ classes if we don’t 
have them already. With those, we can call their action using the same func() function
'''
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
   
    def language(self):
        print("Hindi is the most widely spoken language of India.")
   
    def type(self):
        print("India is a developing country.")
   
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
   
    def language(self):
        print("English is the primary language of USA.")
   
    def type(self):
        print("USA is a developed country.")
  
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
   
obj_ind = India()
obj_usa = USA()
   
func(obj_ind)
func(obj_usa)
###############################
