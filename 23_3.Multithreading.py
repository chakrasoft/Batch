from threading import*
def new():
    for x in range(6):
        print("child executing",current_thread().getName())
    
t1=Thread(target=new)
print(current_thread().getName())

def new():
    for x in range(6):
        print("child executing",current_thread().getName())
    
t1=Thread(target=new)
print(current_thread().getName())
t1.start()


def new():
    for x in range(6):
        print("child executing",current_thread().getName())
    
t1=Thread(target=new)
print(current_thread().getName())
t1.start()
t1.join()
print("bye",current_thread().getName())   


from threading import*

import time
def sqr(n):
    for x in n:
        time.sleep(1)
        print(x%2)
        
def cube(n):
    for x in n:
        time.sleep(1)
        print(x%3)
n=[1,2,3,4,5,6,7]
s=time.time()
t1=Thread(target=sqr,args=(n,))
t2=Thread(target=cube,args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
e=time.time()
print(e-s)    

    