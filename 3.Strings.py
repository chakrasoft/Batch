# Strings defination - alpha, numeric or alpha numeric combination with sigle or double quotes

s1='10'
s2='xyz'
s3='hyd-72'
type(s1)

# String operations
st1='hyderabad.mumbai'
st2='chennai'
str3='   '

# slicing on strings by using indexes whcih starts from 0 for forwad direction and
# for backward direction indexe starts from -1
st1[0]       # return first value in the string
st1[3:6]     # return the values from index 3 to index 5 (end index not include)
st1[-2]      # return value from last 2 nd as its backward reading
st1[2:]      # return all the values from index 2 till end of the string
st1[-6:-1]   # return string from -6 index to -2 index
st1[3] = '77'  # string variable doesn't support to edit the values at specific index.  

# functions on strings
st1='hyderabad.mumbai'

len(st1)
st1.isdigit()
st1.isnumeric()
st1.islower()
st1.isupper()
st1.isalpha()
st1.isalnum()

dir(__builtins__)
help(__builtins__)
#check the object type against target type
x=10
isinstance(x,int) 


st1.capitalize()
st1.upper()
st1.lower()
st1.center(19)
st1.center(20)
st1.center(20,'@')
st1.zfill(20)
t='8765'
t.zfill(20)

st1.count('a') # return no of times substring repeation in main string.
st1.count('y',1,3)  # count substring only in mentioned range


st1.find('k') # retuns the index where the substring is find first else returns -1 
st1.find('b',3,6) # find substring only in mentioned range


# cancatination(+) and repeatation(*) of strings
fname='John'
lname='Kilner'

fname+lname
fname+ ' ' +lname
fname * 2


# tab space, alert , new line in a string

letter = 'dhjkfdgkjhdgjk\t hdfhdsgh\b dgdsg \ajhjdhsgkj \n'
letter 
st1='\n'
print('student name:', letter,st1,'end')


# type conversation 

#from string to int   
x='20'
n= int(x)

print(n)
type(n)

y='20.98'
n= int(y)
# int to string
a=10
st1=str(a)
st1

# String dispaly formats.
age=30
name='kumar'
print(' My name is: {}, age is: {}'.format(name,age))

**************************************************************
s6 = "I contain\t\t\tthree\t\t\ttabs"
s7 = "I contain a\t\v\tvertical tab"
s8 = "I contain a\t\a\tBELL, which you can hear"

print(s6)
print(s7)
print(s8)
