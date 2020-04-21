import os
os.getcwd()
os.chdir("E:\Office\Python\Rk\PYTHON_master\samplefiles")
os.getcwd()

# File modes(r,r+,w,w+,a,a+,etc..)
# Open a file from mentioned path
ft=open('date1209.txt','r')
ft=open('mdata.txt','r')
print(ft.read())

# Write a file
ft=open('mdata.txt','w')
ft.write('line-3')

#close a file 
ft.close()

ft=open('date1200.txt','w')
ft.write('line-2')
ft.write('line-3')
ft.close()

# read full file 
ft=open('date1209.txt','r')
ft.read()
ft.close()

# read file content only specific length data
ft=open('date1209.txt','r')
ft.read(5)
ft.close()

# read total line at a time
ft=open('date1209.txt','r+')
ft.readline()

ft=open('date1209.txt','r+')
ft.readlines()

# write multiple lines at a time
seq=['line-1\n','line-2\n']
ft=open('testfile2108.txt','r+')
ft.write('line-6')
ft.writelines(seq)
ft.write('\n')
ft.close()



# Other file functions
ft=open('date0808.txt','r+')
ft.tell()   # position of the control to read a file position
ft.read(5) 
ft.tell() 
ft.seek(0,1)   # to set the position
ft.tell()
ft.close()
ft=open('date0808.txt','w')
ft.write('line-5')
ft.close()

# to know whether file is closed or not.
ft.closed

#fp.seek(offset, from_what)
'''
where fp is the file pointer you're working with; offset means how many positions 
you will move; from_what defines your point of reference:

0: means your reference point is the beginning of the file
1: means your reference point is the current file position
2: means your reference point is the end of the file
if omitted, from_what defaults to 0.
'''
ft=open('date0808.txt','r')
ft.seek(0,0)   # to set the position
next(ft)
ft.close()

# other file functions to know about file
ft.closed
ft.name
ft.mode
ft.fileno()

'''
# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: "), fo.name

fid = fo.fileno()
print ("File Descriptor: "), fid

# Close opend file
fo.close()
'''

ft=open('date0808.txt','w+')
ft.read(3)
ft.truncate(3)
ft.close()


ft=open('test.txt','a+')
ft.write("end")
ft.read()
ft.read(10)
ft.close()
ft=open('test.txt','r+')
ft.readline()
ft.readlines()
ft.close()
ft=open('test.txt','r+')
print(ft.readline())
ft.flush

#To delete a file you must import os module and run its os.remove() function
import os
os.remove('mdata.txt')

#check the file exists
import os
if  os.path.exists('mdata.txt'):
    os.remove('mdata.txt')
else:
    print('The file does not exist')

#deleting a folder
import os
os.rmdir('x')    

'''########To list all the files and path in the folder###########'''
import glob

path = 'E:\Office\Python\Rk\PYTHON_OCT2018-master2\samplefiles'

files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

for f in files:
    print(f)
##############FILES#############    
files = [f for f in glob.glob("**/*.txt", recursive=True)]

for f in files:
    print(f)
'''
from itertools import islice
with open("datafile") as myfile:
    head = list(islice(myfile, N))
print head


with open("datafile") as myfile:
    head = [next(myfile) for x in range(N)]
print(head)
'''