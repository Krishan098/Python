'''Concurrency is working on multiple things at the same time
        :. Threading: by letting multiple threads take turns.
        :. multiprocessing: we're using multiple processes. 
        :. asynchronous IO: firing off a task and continuing to do other stuff, instead of waiting for an answer from the network or disk
        :. Distributed computing: using multiple computers at the same time.
'''
# A python thread is an independent sequence of execution, but it shares memory with all the other threads belonging to the program.
#Switching happens so fast that it appears they are running side by side at the same time.
# Multiple processes: Process is also an independent sequence of execution.Unlike threads , a process has its own memory space that is not shared with other processes.
# Asynchronous IO : It is a single threaded, single-process paradigm. 
''' I/O bound vs CPU bound problems:
                                                                                                    I/O bound software: software that is mostly waiting for input/output operations to finish, usually when fetching data from the network or from storage media.
        CPU bound software: Software that uses all CPU power to produce the needed results. It maxes out the CPU.
'''

'''
        Python concurrency with threads:
                        While waiting for answers from the network or disk, you can keep the other parts running using multiple threads.
                        Global Interpreter Lock.: Ensures that there is always one thread running, so threads can't interfere with each other. 
                        
                        
        Python concurrency with asyncio:
                        Asyncio is a relatively new core library in Python.
        
'''

''' Python concurrency with multiprocessing: Using multiple processors using multiprocessing.
        :.Using a network of computers to use many processors, spread over multiple machines. We call this distributed computing.
        #The multiprocessing library bypasses the Python threading library.'''

'''PyPy:
        It uses just-in-time compilation(JIT). It combines the speed advantage of ahead-of-time compilation with the flexibility of interpretation.
   Cython:
        It offers C-like performance with code that is written mostly in Python but makes it possible to compile parts of your Python code to C code.
'''
'''GLOBAL INTERPRETER LOCK:
                :.Thread Safety: Python threads share the same memory. With multiple threads running simulatneously, we don't know the order in which the threads access 
                shared data. Therefore, the result of accessing shared data is dependent on the scheduling algorithm. This algo decides which threads run when.
                
                :. Thread-safe code only manipulates shared data in such a way, that it doesnot interfere with other threads.
                
                :.Race condition: The condition of a system where the system's behaviour is dependent on the sequence or timing of other, uncontrollable events.
'''

def heavy(n,myid):
        for x in range(1,n):
                for y in range(1,n):
                        x**y
        print(myid,"is done")

'''BASELINE : single thread execution'''
import time
def heavy(n,myid):
        for x in range(1,n):
                for y in range(1,n):
                        x**y
        print(myid, "is done")
def sequential(n):
        for i in range(n):
                heavy(500,i)
if __name__== "__main__":
        start=time.time()
        sequential(80)
        end=time.time()
        print("Took:",end-start)