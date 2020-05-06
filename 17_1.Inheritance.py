'''
Inheritance is the capability of one class to derive or inherit the properties 
from some another class. The benefits of inheritance are:

--It represents real-world relationships well.
--It provides reusability of a code. We don’t have to write the same code again 
and again. Also, it allows us to add more features to a class without modifying it.
--It is transitive in nature, which means that if class B inherits from another class A, 
then all the subclasses of B would automatically inherit from class A.

1. Single inheritance: When a child class inherits from only one parent class, 
it is called as single inheritance. We saw an example above.

2. Multiple inheritance: When a child class inherits from multiple parent classes, 
it is called as multiple inheritance.

3. Multilevel inheritance: When we have child and grand child relationship.
'''
##################################################################
#Inheritance
class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

a1=A()

a1.feature1()
a1.feature2()
#########################Single level Inhertance##########################
# parent class 
class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

# child class          
class B(A):    # It is child class or subclass -> 
              #Class B is inheriting all the features from class A
       
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")    

# creation of an object variable or an instance          
a1=A()

a1.

# calling a function of the class feature1 using its instance 
a1.feature1()
a1.feature2()

b1=B()

b1. 

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
########################Multi level Inheritance#########################
class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    
         
class B(A):    # It is child class or subclass -> 
              #Class B is inheriting all the features from class A
       
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")    

         
class C(B):     
              #Class C is inheriting all the features from A and class B
       
    def feature5(self):  
         print("Feature 5 working") 
                  
c1=C()

c.

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

#######################Mutilple ##############################

class A:  
     
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    
         
class B:    #Class B is not inheriting all the features from class A
       
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working") 
 
        
class C(A,B):     
              #Class C is inheriting all the features from A and class B
       
    def feature5(self):  
         print("Feature 5 working") 
                  
c1=C()
c1.feature1()

b1=B() 


b1.

#######################################################################
#Constructor in Inheritance

class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

       
class B(A):  
        
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4  working")    

a1=A()   #A() is a constructor
a1.

a1=B()
#########################################################################
#Constructor in Inheritance
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

         
class B(A): 
    
    def __init__(self):  
        print("In B Init")  
                
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")    

a1=A()   #A() is a constructor
a1=B()

a1.
b1.
 
###########   Super is used############################### 
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

      
class B(A):  
    def __init__(self):  
        print("In B Init")  
    
    def feature3(self):  
         print("Feature 3 working") 
         
    def feature4(self):  
         print("Feature 4 working")  

a1=B() 

class B(A):  
    def __init__(self):  
        super().__init__()  #Superclass will call both A and B init
        print("In B Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature4(self):  
         print("Feature 4 working")               

a1=B() 

##################################################
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature2(self):  
         print("Feature 2 working")    

      
class B:  
    def __init__(self):  
        print("In B Init")  
    
    def feature1(self):  
         print("Feature 1 working") 
         
    def feature4(self):  
         print("Feature 4 working")  
         
class C(A,B):  
    def __init__(self):  
        print("In C Init")           

a1=C() 

########################we are not taking B here########################################

class C(A,B):  
    def __init__(self):  
        super().__init__()
        print("In C Init") 

a1=C() 

#####################Method Resolution Order#######################
#Left to rigt
class A:  
    def __init__(self):  
        print("In A Init")  
    
    def feature1(self):  
         print("Feature 1-A working") 
         
    def feature2(self):  
         print("Feature 2 working")  
         
class B:  
    def __init__(self):  
        print("In B Init")  
    
    def feature1(self):  
         print("Feature 1-B working") 
         
    def feature4(self):  
         print("Feature 4 working")     
         
         
class C(A,B):  
    def __init__(self):  
        super().__init__()
        print("In C Init") 

a1=C() 
a1.feature1()

####################OTHER EXAMLES OF INHERITANCE###################################
#single level
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  

'''Multi-Level inheritance is possible in python like other object-oriented languages. 
Multi-level inheritance is archived when a derived class inherits another derived class. 
There is no limit on the number of levels up to which, 
the multi-level inheritance is archived in python.'''

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  

#Python provides us the flexibility to inherit multiple base classes in the child class.

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  

print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  

'''The issubclass(sub, sup) method is used to check the relationships between 
the specified classes. It returns true if the first class is the subclass of 
the second class, and false otherwise.'''
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(issubclass(Derived,Calculation2))  
print(issubclass(Calculation1,Calculation2))  

'''The isinstance() method is used to check the relationship between 
the objects and classes. It returns true if the first parameter, 
i.e., obj is the instance of the second parameter, i.e., class.'''


class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(isinstance(d,Derived))  

#####################################################################
'''#Method Overriding'''

'''We can provide some specific implementation of the parent class method in our child class.
 When the parent class method is defined in the child class with some specific implementation,
 then the concept is called method overriding. We may need to perform method overriding 
 in the scenario where the different definition of a parent class method is needed in 
 the child class.'''
 
 class Animal:  
    def speak(self):  
        print("speaking")  
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
d = Dog()  
d.speak()  


class Bank:  
    def getroi(self):  
        return 10;  
class SBI(Bank):  
    def getroi(self):  
        return 7;  
  
class ICICI(Bank):  
    def getroi(self):  
        return 8;  
b1 = Bank()  
b2 = SBI()  
b3 = ICICI()  
print("Bank Rate of interest:",b1.getroi());  
print("SBI Rate of interest:",b2.getroi());  
print("ICICI Rate of interest:",b3.getroi());  


'''Abstraction is an important aspect of object-oriented programming. In python, 
we can also perform data hiding by adding the double underscore (___) as a prefix to 
the attribute which is to be hidden. After this, the attribute will not be visible outside 
 the class through the object.'''
 
 class Employee:  
    __count = 0;  
    def __init__(self):  
        Employee.__count = Employee.__count+1  
    def display(self):  
        print("The number of employees",Employee.__count)  
emp = Employee()  
emp2 = Employee()  
try:  
    print(emp.__count)  
finally:  
    emp.display()  
    
###########################################################






