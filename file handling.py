# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:42:58 2020

@author: Chakra IT
"""

import os 
print(os.name) 




import os
os.getcwd()
os.chdir("E:\Office\Python\Rk\PYTHON_master\samplefiles")
os.getcwd()



# File modes(r,r+,w,w+,a,a+,etc..)


#to create a empty text file           
my_file = open('xpm.txt', 'w')   


#u can create ur own txt file n do it 

    
# Open a file from mentioned path
ft=open('date1920.txt','r')
ft=open('kdata1.txt','r')
print(ft.read())


# Write a file
ft=open('kdata1.txt','w')
ft.write('line-4')
ft=open('kdata1.txt','r')
print(ft.read())


#close a file 
ft.close()



# read full file 
ft=open('date1920.txt','r')
ft.read()
ft.close()


# read file content only specific length data
ft=open('date1920.txt','r')
ft.read(5)
ft.close()



# read total line at a time
ft=open('date1920.txt','r+')
ft.readline()

ft=open('9pm.txt','r+')
print(ft.read())

ft=open('8pm.txt','r')
print(ft.read())


#This function returns the first 2 characters of the next line.
ft=open('8pm.txt','r')
print(ft.readline(2))

ft=open('8pm.txt','r')
print(ft.readline())


ft=open('8pm.txt','r')
print(ft.readlines())



#we are trying to read only the 4th line from the ‘test.txt’ file using a “for loop”.


line_number = 4
ft = open('8pm.txt', 'r')
currentline = 1
for line in ft:
           if(currentline == line_number):
                       print(line)
                       break
           currentline = currentline +1
          
          

#code writes the String ‘Hello World’ into the ‘test.txt’ file. 
           
#to create a empty text file           
my_file = open('xpm.txt', 'w')       
           
my_file = open('8pm.txt', 'w')
#my_file.write('Hello World') 
my_file.write('hellooo')
my_file = open('8pm.txt', 'r')  
print(my_file.read())
print(my_file.readlines())  


my_file = open('8pm.txt', 'w')
my_file.write('Hello world\n')
my_file.write('hhi')
my_file = open('8pm.txt', 'r')  
print(my_file.read())  
          
          
 #code writes a list of data into the txtfile         
fruits = ['Apple\n', 'Orange\n', 'Grapes\n', 'Watermelon']
my_file = open('8pm2.txt', 'w')
my_file.writelines(fruits) 
  
my_file = open('8pm2.txt', 'r') 
print(my_file.read())     
          

#appends the string ‘strawberry’ at the end of the txtfile

my_file = open('8pm2.txt', 'a+')
my_file.write ('Strawberry')        


my_file = open('8pm2.txt', 'r') 
print(my_file.read())     


#appends the string ‘guava’ at the end of the ‘txt’ file in a new line.



my_file = open('8pm2.txt', 'a+')
my_file.write ('\nGuava')

my_file = open('8pm2.txt', 'r') 
print(my_file.read())     




# appends a list of data into a ‘txt’ file.

fruits = ['\nBanana', '\nAvocado', '\nFigs', '\nMango']
my_file = open('8pm2.txt', 'a+')
my_file.writelines(fruits)


#tell() method which prints where the cursor is currently at.

print("where the file cursor is:",my_file.tell())

my_file.seek(0)
for line in my_file:
      print(line)
my_file.close()

my_file = open('8pm2.txt', 'r') 
print(my_file.read())     
my_file.close()

os.rename('8pm2.txt', '8pm4.txt')
my_file=open('8pm4.txt','r')
print(my_file.read())

os.remove('8pm4.txt')


#File encoding represents converting characters into a specific format
# which only a machine can understand
my_file = open('8pm3.txt', mode='r')
print('Microsoft Windows encoding format by default is:', my_file.encoding)
my_file.close()

#File I/O Attributes


my_file = open('8pm4.txt', 'a+')
print('What is the file name? ', my_file.name)
print('What is the file mode? ', my_file.mode)
print('What is the encoding format? ', my_file.encoding)
print('Is File closed? ', my_file.closed)

my_file.close()
print('Is File closed? ', my_file.closed)











