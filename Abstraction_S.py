'''
Abstraction focuses on hiding the internal implementations of a process 
or method from the user. In this way, the user knows what he is doing but 
not how the work is being done.
'''
#####################################################
class abs_class:
    def method(self):
        print("ChakraIT")
     #abstract methods

class abs_class:
    def method(self):
        pass     #I do not have anything inside this method
        
#The method which only has a declaration but not a definition wecall abstract method
#A class which has abstract methods are abstract classes
#Does not support abstract classes      

class abs_class:
    def method(self):
        pass 

ab=abs_class()
ab.method()
##############################33
from abc import ABC
class abs_class(ABC):
     #abstract methods

#################
'''
from abc import ABC, abstractmethod
class abs_class(ABC):
    #normal method
    def method(self):
        #method definition
    @abstractmethod
    def Abs_method(self):
        pass
        #Abs_method definition
'''
#################
from abc import ABC, abstractmethod
class abs_class(ABC):
    @abstractmethod
    def Abs_method(self):
        pass  #Abs_method definition   
      
c1=abs_class()
c1.Abs_method()

#################
from abc import ABC, abstractmethod
class abs_class(ABC):
    @abstractmethod
    def Abs_method(self):
        pass  #Abs_method definition   

class abs_section(abs_class):
    pass
    
        
#c1=abs_class()
c2=abs_section()
#################Ex1########################
from abc import ABC, abstractmethod
class abs_class(ABC):
    @abstractmethod
    def abs_method(self):
        pass  #Abs_method definition   

class abs_section(abs_class):
    def abs_method(self):
        print("Its working")
        
#c1=abs_class()
c2=abs_section()
c2.abs_method()
#################Ex2###########################
from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass  #Abs_method definition   

class Laptop(Computer):
    def process(self):
        print("Its working")
        
#c1=abs_class()
c2=Laptop()
c2.process()

#################Ex3###########################
from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass  #Abs_method definition   

class Laptop(Computer):
    def process(self):
        print("Its working")
        
      
class Developer:
    def work(self):
        print("Resolving Erros")
      
        
#c1=abs_class()
c2=Laptop()
c2.process()

d1=Developer()
d1.work()

###############################################
from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass  #Abs_method definition   

class Laptop(Computer):
    def process(self):
        print("Its working")
        
class Whiteboard:
    def write(self):
        print("Its working")
        
class Developer:
    def work(self,com):
        print("Resolve Erros")
        com.process()
        
#c1=abs_class()
c2=Laptop()
c2.process()

d1=Developer()
d1.work(c2)

###############################################
from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass  #Abs_method definition   

class Laptop(Computer):
    def process(self):
        print("Its working")
        
class Whiteboard:
    def write(self):
        print("Its working")
        
class Developer:
    def work(self,com):
        print("Resolve Erros")
        com.process()
        
#c1=abs_class()
c2=Laptop()
c3.Whiteboard()

d1=Developer()
d1.work(c3)
#If someone wnats to use your API then they need to define all the methods
'''
As a property, abstract classes can have any number of abstract methods 
coexisting with any number of other methods.

method() is normal method whereas Abs_method() is an abstract method 
implementing @abstractmethod from the abc module.
'''
from abc import ABC, abstractmethod
class abs_class(ABC):
    #normal method
    def method(self):
        #method definition
    @abstractmethod
    def Abs_method(self):
        #Abs_method definition
        
##############################
from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
 
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
 
class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")
 
#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
 
#object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)
 
print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))


'''
Absclass is the abstract class that inherits from the ABC class from 
the abc module. It contains an abstract method task() and a print() method 
which are visible by the user. Two other classes inheriting from this 
abstract class are test_class and example_class. Both of them have their 
own task() method (extension of the abstract method).

After the user creates objects from both the test_class and example_class 
classes and invoke the task() method for both of them, the hidden definitions
for task() methods inside both the classes come into play. These definitions 
are hidden from the user. The abstract method task() from the abstract class 
Absclass is actually never invoked.

But when the print() method is called for both the test_obj and example_obj, 
the Absclass’s print() method is invoked since it is not an abstract method.
'''



     