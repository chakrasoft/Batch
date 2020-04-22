# Random Functions
'''Choice - A random item from a list, Tuple, String
Randrange - A randomly selected variable from ranges(start,stop,step)
random -A random float r, Such that 0 is less than or equal to r  and r is less than 1
randint - genearte radon interger for given range (doesnt work for float values)
seed - sets the integer starting value use in generating random numbers. Call this function 
before calling any other random module function. returns none
Shuffle - Randomizes the items of a list in place. Returns none
Uniform(x,y) - A random float r, such that x is less than  or equal to r and r is less than y
'''
import random
import random as rd

print(dir(rd))  # see all random functions
print(help(rd.random))
print(help(rd.choice))

print("randon number from range(100) :", rd.choice(range(100)))
l1 = [1,2,3,4,5,6]
print("randon element from l1 :", rd.choice(l1))
str="Hello World"
print("randon chracter from srting :", rd.choice(str))
a =rd.choice([1,2,3,4,5,6])
a

# generate a random interger number in given range 
#randrange(start,stop,step)
print("randrange(1,100,2) :", rd.randrange(1,100,2))
print("randrange(100) :", rd.randrange(100))
d=rd.randrange(10,100)
d

# generate a random interger number with given step
e=rd.randrange(10,100,5)
e

# Generate random float number between 0<=random<1
print("random() :", rd.random())
b=rd.random()  
b

#Display 10 random numbers from interval(0,1)
for i in range(10):
    print(rd.random())

# genearte radon interger for given range (doesnt work for float values)
#it include last item and no step but in randrange not include last item and have step.
c=rd.randint(2,6)  
c

dice=rd.randint(1,6) 
dice

if dice==1:
    print("You Win")
else:
    print("You loose" ,dice)


# Generate random floating number in given range 
f = rd.uniform(3,5)  
f
print("random float uniform(3,5)", rd.uniform(3,5))
print("random float uniform(7,14)", rd.uniform(7,14))


#Shuffle values in l1
rd.shuffle(l1)
l1

# seed means random number will be fixed for that particular seed value.
x1= rd.random()
x1

rd.seed()
print("random number with default seed", rd.seed())
rd.seed(10)
print("random number with int seed", rd.random())
rd.seed("Hello,2")
print("random number with str seed", rd.random())

rd.seed(5)
x2= rd.random()
x2

rd.seed(5)
x2= rd.random()
x2

rd.seed(7)
x3= rd.random()
x3

rd.seed(1)
x4= rd.random()
x4

rd.seed(5)
x9= rd.random()
x9

rd.seed(3)
x6= rd.random()
x6

rd.seed(7)
x7= rd.random()
x7

####################################################################
rd.seed(3) 
  
# print a random number between 1 and 1000. 
print(rd.randint(1, 1000)) 
  
# if you want to get the same random number again then, 
rd.seed(3)  
print(rd.randint(1, 1000)) 
  
# If seed function is not used 
  
# Gives totally unpredictable response. 
print(rd.randint(1, 1000)) 

#normal variate

normalvariate(mean, std_dev)


for i in range(10):
    print(rd.normalvariate(0,1))
    
    
    
