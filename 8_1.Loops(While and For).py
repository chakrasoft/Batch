'''
The while Loop
With the while loop we can execute a set of statements as long as a condition is true.
'''
i = 1
while i < 6:
    print(i)
    i += 1
  
#Note: remember to increment i, or else the loop will continue forever.

'''
The break Statement
With the break statement we can stop the loop even if the while condition is true:
'''
#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

'''
The continue Statement
With the continue statement we can stop the current iteration, and continue with the next:
'''
#Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

##############################FOR####################################################
'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more 
like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, 
tuple, set etc.    
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  
  
#The for loop does not require an indexing variable to set beforehand
  
for x in "banana":
  print(x)

'''
The break Statement
With the break statement we can stop the loop before it has looped through all the items:
    '''
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

'''
The continue Statement
With the continue statement we can stop the current iteration of the loop, 
and continue with the next:
''' 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

'''
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and ends at a specified number.
'''
for x in range(6):
  print(x)
'''  
Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
The range() function defaults to 0 as a starting value, however 
it is possible to specify the starting value by adding a parameter: range(2, 6), 
which means values from 2 to 6 (but not including 6):
'''
  
for x in range(2, 6):
  print(x)

''' 
The range() function defaults to increment the sequence by 1, however it is possible to 
specify the increment value by adding a third parameter: range(2, 30, 3): 
'''

for x in range(2, 30, 3):
  print(x)

#Else
    
for x in range(6):
  print(x)
else:
  print("Finally finished!")    
    
'''
Nested Loops
############
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

'''    
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content,
 put in the pass statement to avoid getting an error.
 '''
 
 for x in [0, 1, 2]:
  pass


# Looping programs(To avoid repeated )
#If you want to print 10 times (Print 1 to 10)

count=1
while (count <=10):
    print(count)

count=1
while count <=10:
    print(count)
    count=count+1

FOR
****
for i in range(1,11): 
# It will not consider the last 11
    print(i)
    print(9)
    
for i in range(-5,11): 
# It will not consider the last 11
    print(i)
    print(9)

#i is a tempory variable

#if i want to print even number or only odd number then its tough

# while Loops

count = 1
while count < 3:
    name = input('enter student name: ')
    marks = int(input('enter student marks: '))
    print('student name----: ', name, 'Marks----: ', marks)
    count = count + 1
print('end of while and count is:', count)

cont = 'y'
while cont == 'y':
    name = input('enter student name: ')
    marks = int(input('enter student marks: '))
    print('student name----: ', name, 'Marks----: ', marks)
    cont=input('want to continue -y- else press any other')
print('end of while and count is:', cont)


count = 0
while (count < 3):    
    count = count+1
    print("Hello python:", count)
    
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
computer_brands[0]
computer_brands[1]
computer_brands[2]
computer_brands[3]

len(computer_brands)

computer_brands = ["Apple", "Asus", "Dell", "Samsung"]

i = 0
while i < len(computer_brands): # i < 4
    print (computer_brands[i])
    i = i + 1
print('sucessfull')

    
#For Loops

for i in range(0,100):
    print(i)
print('range for loop done sucessfully')    


l1 = [1,2,3,4,5,6]
for i in l1:
    print(i)
print('for loop done sucessfully' )
    
#Examples
computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
for brands in computer_brands:
    print (brands)

numbers = [1,10,20,30,40,50]
sum = 0
for number in numbers:
    sum = sum + number
print (sum)
###########################################
for i in range(1,10):
    print (i)
    
li = [4,5,6,2,9,1]    
for i in range(0, len(li)):
    print (li[i], end="     ")
############################################
#1
#2   2
#3   3   3
#4   4   4   4
#5   5   5   5   5

for i in range(10):
     print(i)
else:
     print("Reached else")
     
for i in range(10):
        print(i)
        if(i==7): break
else: print("Reached else")
##################ALL STARS###############################
for i in range(1,6):
        for j in range(i):
            print("*",end=' ')
        print()
#####################################
for i in range(5):
       
    print(i)
######################################
for i in range(1, 6):
 print(i)
########################################### 
for i in range(1, 6):
    for j in range(i):
         print(j, end=' ')
    print()

#################################################
x=int(input("How many cholates you want"))    

i=1
while i<=x:
        
    print("Cholates")
    i+=1

#Break statement
c=5
x=int(input("How many cholates you want"))    

i=1
while i<=x:
    if i>c:
        break
    print("Cholates")
    i+=1

print("Bye")
#################################################
c=5
x=int(input("How many cholates you want"))    

i=1
while i<=x:
    if i>c:
        print("Out of Stock")
        break
    print("Cholates")
    i+=1

print("Bye")
##################################################
# continue statement
for i in range(1,10):
    
        print(i)
###################we will get error########################
for i in range(1,10):
    if i%3==0:
        
    print(i)
        
print("Bye")
##########################use continue#########################
for i in range(1, 10):
    if i%3==0:
        continue
    print(i)
        
print("Bye")
#############################################
for i in range(1, 10):
    if i%3==0 or i%5==0:
        continue
    print(i)
        
print("Bye")
###################################################
for i in range(1, 10):
    if i%3==0 and i%5==0:
       continue
    print(i)
        
print("Bye")
##########################################
#pass statement
for i in range(1,101):
    if(i%2!=0):
       pass
    else:
        print(i)

print("Bye")
##############################################
# continue statement
# Prints all letters except 'e' and 's'
for letter in 'chakra': 
    if letter == 'e' or letter == 's':
         continue
    print ('Current Letter :', letter)

#Break statement
for letter in 'chakra': 
 
    # break the loop as soon it sees 'e' 
    # or 's'
    if letter == 'e' or letter == 's':
         break
 
print ('Current Letter :', letter)  

#pass statement
for letter in 'chakra':
    pass
print ('Last Letter :', letter)

# Write tables.
for x in range(1, 11):
    for y in range(1, 11):
        print ('%d * %d = %d' % (x, y, x*y))  