# define the numbers
a=20
b=40

# Number types - Interger, float, complex and long
x = 10
y = 2.50
#z=123456l
#z=2+4j
type(x)

'''
complex = (3 - 4j)
print('Magnitude of 3 - 4j is:', abs(complex))
'''

# adding of a,b & line continution  
a= 10
c=20
a+c
tot=a+b
print(tot)

#Dont give space after \
sum1 = a+ \
    b
print(sum1)
  
sum1= a+b
print(sum1)

a=20
b=3
a/b
a%b
a//b

# Assigmnet types - Below both statemtns are same 
a = a+b
a+=b
print(a)

a=1
b=c=s=g=2
d,e,f = 3,4,'xyz'
print('a: ',a,'b: ',b,'c: ',c,'d: ',d,'e: ',e,'f: ',f,'s: ',s,'g: ',g)
print('THE FIRST SOL',a \
      ,b )
#To find the variable type 
type (a)

#Number functions on Numbers
tot = a-b
print(tot)
abs(tot)

integer = -20
print('Absolute value of -20 is:', abs(integer))

round(30.45)
round(30.456,2)
round(30.55)
max(3,1,56,99,3,4,6)
min(3,1,56,99,3,4,6)
x=100
y=4
p=pow(x,y)
p=x**y
print(p)

print('Pow value is:', x**y)

# Math functions
#import math as mt
import math
math.
math.ceil(30.55)
math.floor(30.55)
math.sqrt(49)

# delete a Number / variable
x=1
print (x)
del x
print(x)


# Examples of Bitwise operators 
a = 10
b = 4
  
# Print bitwise AND operation   
print(a & b) 
  
# Print bitwise OR operation 
print(a | b) 
  
# Print bitwise NOT operation  
print(~a) 
  
# print bitwise XOR operation  
print(a ^ b) 
  
# print bitwise right shift operation  
print(a >> 2) 
  
# print bitwise left shift operation  
print(a << 2) 

'''
0 is written as "0"
1 is written as "1"
2 is written as "10"
3 is "11"
4 is "100"
5 is "101"
.
.
1029 is "10000000101" == 2**10 + 2**2 + 2**0 == 1024 + 4 + 1'''