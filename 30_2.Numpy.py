# Python program to demonstrate  
# basic array characteristics 
'''
Numpy - Numerical Python
numpy vs list
numpy operators
numpy functions
#Numpy is the core library for Scientific computing in Python
#It provides a high performance multidimentional array object, and tools for working 
with these arrays
n dimensional array object
linear Algebra
multidimentional container for data
randon number capabilities

6 types of arrays
array()
linspace()
logspace()
arange()
zeros()
ones()
'''

val =int(input("enter the value for search"))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    
    K+=1

print(arr.index(val))
#########################error as array does not support##################################
from array import *

arr = array('i',[1,2,3],[4,5,6])

print(arr)
###################error#########################
from numpy import *

arr = array('i',[1,2,3],[4,5,6])

print(arr)
########################No need to mention the type####################
from numpy import *

arr = array([1,2,3,4,5,6],int)

print(arr)
print(arr.dtype) #It give the type of array
#############################float#######################
from numpy import *

arr = array([1,2,3,4,5,6.0])
arr = array([1,2,3,4,5,6.0],float)

print(arr)
print(arr.dtype) #It give the type of array

####################################################
from numpy import *

arr = linspace(0,15,10) 

print(arr)
print(arr.dtype) #It give the type of array
####################################################
arr = arange(1,15,2) # first,last,steps

print(arr)
####################################################

arr = logspace(1,20,5) # first,last,steps

print(arr)   #check the first number and last number in range
#######################################

arr = logspace(1,20,5) # first,last,steps

print(arr)
print('%.2f' %arr[0])
print('%.2f' %arr[4]) # you can change the value here
                        # five parts
####################################################
arr = zeros(4) # giving float

print(arr)   #gives all the numbers as zero
####################################################
arr = ones(4) # giving float
arr = ones(4,int)
print(arr)   # It gives you ones
####################ADD###################################
arr = array([1,2,3,4,5])

arr=arr+5

print(arr)
######################################################
arr1 = array([1,2,3,4,5])
arr2 = array([5,6,8,4,2])

arr3=arr1+arr2
print(arr3)
######################################################
arr = array([1,2,3,4,5])

print(sin(arr))
print(tan(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

######################################################
arr1 = array([1,2,3,4,5])
arr2 = array([5,6,8,4,2])

print(concatenate([arr1,arr2]))
####################copy##################################
arr1 = array([1,2,3,4,5])

arr2=arr1
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
################################################
arr1 = array([1,2,3,4,5])

arr2=arr1.view()  #nhelp you to create a different --here the address is different
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
##################shallow copy##############################

arr1 = array([1,2,3,4,5])      #copy the elements  if you change the value 26813

arr2=arr1.view()
arr[1]=7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
##################deep copy##############################

arr1 = array([1,2,3,4,5]) #changes are reflected in first arry not on the second

arr2=arr1.copy()
arr[1]=7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
#######################Two Dimentional array################################
arr1 = array([
               [1,2,3],
               [4,5,6]
            ])
print(arr1.shape)  # It give 2 rows and 3 columns

print(arr1.size) 

#####################2D array to 1D array######################################
arr1 = array([
               [1,2,3],
               [4,5,6]
            ])

arr2=arr1.flatten()
print(arr2)
##################### 1D array to 2D array ######################################
arr1 = array([
               [1,2,3,6,2,9],
               [4,5,6,7,11,12]
            ])

arr2=arr1.flatten()
arr3=arr2.reshape(3,4) 
arr4=arr2.reshape(2,2,3)  #2 rows , 2 rows and 3 columns
print(arr4)
###############################Matrices#####################################
# Metrices are dimentional arrays
arr1 = array([
               [1,2,3,6],
               [4,5,6,7]
            ])

m=matrix(arr1)
print(m)
###########################################
m=matrix('1,2,3;6,4,5;7,8,9')
print(m)
######################print diagnal#####################
m=matrix('1,2,3;6,4,5;7,8,9')
print(diagonal(m))
print(m.max())
###################################################
m1=matrix('1,2,3;6,4,5;7,8,9')
m2=matrix('1,2,3;7,4,2;5,9,6')

m3=m1*m2

print(m3)
#######################################################






























