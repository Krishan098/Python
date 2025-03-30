import time 
import multiprocessing
def heavy(n,myid):
    for x in range(1,n):
        for y in range(1,n):
            x**y
    print(myid,"is done")
# def multiproc(n):
#     processes=[]
#     for i in range(n):
#         p=multiprocessing.Process(target=heavy,args=(500,i,))
#         processes.append(p)
#         p.start()
#     for p in processes:
#         p.join()
# if __name__=='__main__':
#     start=time.time()
#     multiproc(80)
#     end=time.time()
#     print("Took:",end-start)
    
'''Python multiprocessing pool:
            multiprocessing.Pool(p) helper creates a pool of size p processes.
            Pool.map() allows us to submit work to the pool.
'''
def doit(n):
    heavy(500,n)
def pooled(n):
    with multiprocessing.Pool() as pool:
        pool.map(doit,range(n))
if __name__=='__main__':
    start=time.time()
    pooled(80)
    end=time.time()
    print("Pool Took:",end-start)
