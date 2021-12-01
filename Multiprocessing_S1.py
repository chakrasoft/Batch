import multiprocessing 
import time

start =time.perf_counter()
   
def perform(): 
    print('walking 1 sec..') 
    time.sleep(1)
    print('Done walking....') 
    
perform()


finish =time.perf_counter()

print(f'finished in {round(finish-start, 2)} second(s)') 


###############
start =time.perf_counter()
   
def perform(): 
    print('walking 1 sec..') 
    time.sleep(1)
    print('Done walking....') 
    
perform()
perform()

finish =time.perf_counter()

print(f'finished in {round(finish-start, 2)} second(s)') 
##########################################

import multiprocessing 
import time

start =time.perf_counter()
   
def perform(): 
    print('walking 1 sec..') 
    time.sleep(1)
    print('Done walking....') 
    
p1=multiprocessing.Process(target=perform)
p2=multiprocessing.Process(target=perform)

finish=time.perf_counter()

print(f'finished in {round(finish-start,2)} second(s)') 

###################################################
import multiprocessing 
import time

start =time.perf_counter()
   
def perform(): 
    print('walking 1 sec..') 
    time.sleep(1)
    print('Done walking....') 
    
p1=multiprocessing.Process(target=perform)
p2=multiprocessing.Process(target=perform)

p1.start()
p2.start()

finish=time.perf_counter()

print(f'finished in {round(finish-start,2)} second(s)') 
######################################################
import multiprocessing 
import time

start =time.perf_counter()
   
def perform(): 
    print('walking 1 sec..') 
    time.sleep(1)
    print('Done walking....') 
    
p1=multiprocessing.Process(target=perform)
p2=multiprocessing.Process(target=perform)

p1.start()
p2.start()

p1.join()  #
p2.join()

finish=time.perf_counter()

print(f'finished in {round(finish-start,2)} second(s)') 
##################without stsrt and join#####################################
import multiprocessing 
import time

start =time.perf_counter()
   
def perform(): 
    print('walking 1 sec..') 
    time.sleep(1)
    print('Done walking....') 
    
processes=[]

for _ in range(10):   # _ throughaway variable name
    p=multiprocessing.Process(target=perform)
    p.start()
    processes.append(p)

for process in processes:
    process.join() #It will wait until it finishes

finish=time.perf_counter() #Calculates the finishtime

print(f'finished in {round(finish-start,2)} second(s)') 

###################passing arrguments how long to sleep######################
import multiprocessing 
import time

start =time.perf_counter()
   
def perform(seconds): 
    print('walking {seconds} second(s)..') 
    time.sleep(seconds)
    print('Done walking....') 
    
processes=[]

for _ in range(10):
    p=multiprocessing.Process(target=perform, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finishstart=time.perf_counter()

print(f"finished in {round(finishstart,2)} second(s)") 
'''
The arguments should be serialised -> serialising pickle ->Converting 
python Objects into a format that can be deconstructing and reconstructed 
in another python script
'''
###########################################
import concurrent.futures 
import time

start =time.perf_counter()
   
def perform(seconds): 
    print('walking {seconds} second(s)..') 
    time.sleep(seconds)
    return 'Done walking....'
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    f1=executor.submit(perform, 1)
    print(f1.result())
#If you want to use function once at a time then we can use submit method
#submit method schedules a function to be executed and returns a future object

''' 
Future object is basically encaptulates the execution of our function and 
allows us to check on it has scheduled or ran
'''

finish=time.perf_counter()

print(f"finished in {round(finish-start,2)} second(s)") 
###########################################
import concurrent.futures 
import time

start =time.perf_counter()
   
def perform(seconds): 
    print('walking {seconds} second(s)..') 
    time.sleep(seconds)
    return 'Done walking....'
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    f1=executor.submit(perform, 1)
    f2=executor.submit(perform, 1)
    
    print(f1.result())
    print(f2.result())
#If you want to use function once at a time then we can use submit method
#submit method schedules a function to be executed and returns a future object

''' 
Future object is basically encaptulates the execution of our function and 
allows us to check on it has scheduled or ran
'''

finish=time.perf_counter()

print(f"finished in {round(finish-start,2)} second(s)") 
##################################################
import concurrent.futures 
import time

start =time.perf_counter()
   
def perform(seconds): 
    print('walking {seconds} second(s)..') 
    time.sleep(seconds)
    return 'Done walking....'
    
with concurrent.futures.ProcessPoolExecutor() as executor:
    results=[executor.submit(perform,1) for _ in range(10)]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    


finish=time.perf_counter()

print(f"finished in {round(finish-start,2)} second(s)") 
#################Threading VS Processing############################################
from threading import Thread
import os
import math

def calc():
	for i in range(0, 4000000):
	   math.sqrt(i)
threads =[]

for i in range(os.cpu_count()):
	print('registering thread %d' % i)
	threads.append(Thread(target=calc))

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

#************************************************************
from multiprocessing import Process
import os
import math

def calc():
	for i in range(0, 70000000):
	   math.sqrt(i)
processes =[]

for i in range(os.cpu_count()):
	print('registering process %d' % i)
	processes .append(Process(target=calc))

for process in processes:
	process.start()

for process in processes:
	process.join()



