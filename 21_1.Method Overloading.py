# Python doent support method overloading like C++ 
'''2 methods with same name with different parmeters and 
different arguments it is method overloading

If we write the methods with different argument but python 
will consider only latest one.
'''
###################Magic Methods##################
a=4
b=8
print(a+b)
print(int.__add__(a,b))   #behind the scene a+b is called
int.           #int is from the int class in which all the methods are available

a='abc'
b='xyz'
print(a+b)

a='4'
b='8'
print(a+b)
#In programming we use methods for the above
########################passing 2 parameters#########################################
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
        
a1=Student(20,30)
a2=Student(20,40)
a3=a1+a2

class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
        
a1=Student(20,30)
a2=Student(20,40)
s3=a1+a2
print(s3.m1)
print(s3.m2)

#####################
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
        
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    
    def __gt__(self,other):
        b1=self.m1+other.m2
        b2=self.m1+other.m2
        if b1>b2:
            return True
        else:
            return False
        
a1=Student(20,30)
a2=Student(20,40)
s3=a1+a2
print(s3.m1)
print(s3.m2)


if a1>a2:
    print("S1 wins")
else:
    print("S2 wins")

################################
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
        
    def sum(self,a,b):
        a1=a+b
    
        return a1

a1=Student(20,30)
print(a1.sum(5,6))
##################passing 3 parameters will not work############################
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
        
    def sum(self,a,b):
        a1=a+b
    
        return a1

a1=Student(20,30)
print(a1.sum(5,6,3))
####################################
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
        
    def sum(self,a,b,c):
        a1=a+b+c
    
        return a1

a1=Student(20,30)
print(a1.sum(5,6,3))
########################How do we solve this error #############
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
        
    def sum(self,a,b,c):
        a1=a+b+c
    
        return a1

a1=Student(20,30)
print(a1.sum(5,6))
#########################################################
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2
        
    def sum(self,a=None,b=None,c=None):
        a1=0
        if a!=None and b!=None and c!=None:
            a1=a+b+c
        elif a!=None and b!=None:
            a1=a+b
        else:
            a1=a
            
        return a1

a1=Student(20,30)
print(a1.sum(5,6,7))
print(a1.sum(5,6))
print(a1.sum(5))
#######################################################


#################################################################

def student(a,b):
    print(a+b)

def addition(a,b,c):
    print(a+b+c)

add(3,4) 

#############################################
def addition(a,b):
    print(a+b)

def addition(a,b,c):
    print(a+b+c)

add(3,4) 

# But we can code the function behaviur differently as below.   
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print ('Hello ' + name)
        else:
            print ('Hello ')

# Create instance
obj = Human()

# Call the method with out parameter
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')
#########################################################
