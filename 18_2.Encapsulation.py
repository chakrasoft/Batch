# data / method -  Encapsulation/Abstraction /Hide 
'''We can restrict to variables and methods is Encapsulation'''

'''######To prevent the data being modified accidently
Access specifiers -
Private and Public
Private methods are not accessable outside the class###############'''

########################Protected members#############################

class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("Driving")
    def __updatesoftware(self):
        print("Update Software")

rcar=car()
rcar.drive()
##################################################
class car:
    #def __init_(self):
        #self.__updatesoftware()
    def drive(self):
        print("Driving")
    def __updatesoftware(self):    #Can't ccess the private method outside the class
        print("Update Software")

rcar=car()
rcar.drive()
rcar.__updatesoftware()
#####################################################
'''Private variables can modify only inside the class methods
we cannot modify private variables outside the class '''

class car:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed=200
        self.__name="Supercar"
    def drive(self):
        print("Driving")
        print(self.__maxspeed)
    def setspeed(self,speed):       #modifying the private varible
        self.__maxspeed=speed
        print(self.__maxspeed)

redcar=car()
redcar.drive()
redcar.setspeed('100')
################################################

class car:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed=200
        self.__name="Supercar"
    def drive(self):
        print("Driving")
        print(self.__maxspeed)
    #def setspeed(self,speed):
       # self.__maxspeed=speed
       # print(self.__maxspeed)

redcar=car()
redcar.drive()
redcar.__maxspeed=100 
redcar.drive()
#######################################################

class car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color
    
ford=car(200,'red')
ford.speed=300
ford.speed='abcd'
print(ford.speed)
######################To encapsulate ########################

class car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color
        
    def set_speed(self,value):
        self.speed=value
        
    def get_speed(self):
        return self.speed
      
    
ford=car(200,'red')
ford.set_speed(300)
print(ford.get_speed)
print(ford.color)
###########################################
'''We use getters & setters to add validation logic around getting and setting a value.
To avoid direct access of a class field i.e. private variables cannot be accessed directly 
or modified by external user.
Using normal function to achieve getters and setters behaviour

To achieve getters & setters property, if we define normal get() and set() methods 
it will not reflect any special implementation. 
'''

class abc: 
    def __init__(self, age = 0): 
         self._age = age 
      
    # getter method 
    def get_age(self): 
        return self._age 
      
    # setter method 
    def set_age(self, x): 
        self._age = x 
  
raj = abc() 
  
# setting the age using setter 
raj.set_age(21) 
  
# retrieving age using getter 
print(raj.get_age()) 
  
print(raj._age) 
######################################################
'''
Using property() function to achieve getters and setters behaviour

In Python property()is a built-in function that creates and returns a property object. 
A property object has three methods, getter(), setter(), and delete(). property() function 
in Python has four arguments property(fget, fset, fdel, doc), fget is a function for 
retrieving an attribute value. fset is a function for setting an attribute value. fdel 
is a function for deleting an attribute value. doc creates a docstring for attribute. 
A property object has three methods, getter(), setter(), and delete() to specify fget, 
fset and fdel individually.
'''
class chak: 
     def __init__(self): 
          self._age = 0
       
     # function to get value of _age 
     def get_age(self): 
         print("getter method called") 
         return self._age 
       
     # function to set value of _age 
     def set_age(self, a): 
         print("setter method called") 
         self._age = a 
  
     # function to delete _age attribute 
     def del_age(self): 
         del self._age 
     
     age = property(get_age, set_age, del_age)  
  
mark = chak() 
  
mark.age = 10
  
print(mark.age) 
##########################################################
'''
Using @property decorators to achieve getters and setters behaviour

In previous method we used property() function in order to achieve getters and setters 
behaviour. However as mentioned earlier in this post getters and setters are also used 
for validating the getting and setting of attributes value. There is one more way to 
implement property function i.e. by using decorator. Python @property is one of the built-in
 decorators. 

The main purpose of any decorator is to change your class methods or attributes in such 
a way so that the user of your class no need to make any change in their code.
'''
class abcd: 
     def __init__(self): 
          self._age = 0
       
     # using property decorator 
     # a getter function 
     @property
     def age(self): 
         print("getter method called") 
         return self._age 
       
     # a setter function 
     @age.setter 
     def age(self, a): 
         if(a < 18): 
            raise ValueError("Sorry you age is below eligibility criteria") 
         print("setter method called") 
         self._age = a 
  
mark = abcd() 
  
mark.age = 19
  
print(mark.age) 
######################################################






  