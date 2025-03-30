import threading 
import time
def heavy(n,myid):
    for x in range(1,n):
        for y in range(1,n):
            x**y
    print(myid,"isdone")
def threaded(n):
    threads=[]
    for i in range(n):
        t=threading.Thread(target=heavy, args=(500,i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
if __name__=="__main__":
    start=time.time()
    threaded(80)
    end=time.time()
    print("Took:",end-start)

'''An IO-Bound Python threading example
        Each thread takes turns instead of running all at once. 
'''
def heavy_two(n, myid):
    time.sleep(2)
    print(myid,"isdone")
def threaded_two(n):
    threads=[]
    for i in range(n):
        t=threading.Thread(target=heavy_two,args=(500,i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
if __name__=="__main__":
    start=time.time()
    threaded_two(80)
    end=time.time()
    print("Took:",end-start)
    
        