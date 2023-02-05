import threading

def increment(x, y):
    return x + y 

def thread_task_1(lock):
    lock.acquire()
    res = increment(0, 1)
    lock.release()
    print('Response from thread 1', res)

def thread_task_2(lock):
    lock.acquire()
    res = increment(0, 2)
    lock.release()
    print('Response from thread 2', res)

def main_task():

    # creating a lock
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=thread_task_1, args=(lock,))
    t2 = threading.Thread(target=thread_task_2, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()

if __name__ == "__main__":
    #execute main task multiple times to check if they are successfull
    for i in range(5):
        main_task()
        print()
        
'''
Output
$ python multithread.py 
Response from thread 1 1
Response from thread 2 2

Response from thread 1 1
Response from thread 2 2

Response from thread 1 1
Response from thread 2 2

Response from thread 1 1
Response from thread 2 2

Response from thread 1 1
Response from thread 2 2
'''

#Use of locks https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
# Advantages:
# It doesn’t block the user. This is because threads are independent of each other.
# Better use of system resources is possible since threads execute tasks parallely.
# Enhanced performance on multi-processor machines.
# Multi-threaded servers and interactive GUIs use multithreading exclusively.

# Disadvantages:
# As number of threads increase, complexity increases.
# Synchronization of shared resources (objects, data) is necessary.
# It is difficult to debug, result is sometimes unpredictable.
# Potential deadlocks which leads to starvation, i.e. some threads may not be served with a bad design
# Constructing and synchronizing threads is CPU/memory intensive.