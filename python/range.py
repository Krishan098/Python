'''------------------RANGE---------------------------------
        Can be used to create sequences of numbers.
        acts as a built-in function and is commonly used for looping a specific number of times.
        :.range(stop)
        :.range(start,stop)
        :.range(start,stop,step) 
        can have a negative step size
''' 
my_range=range(3)
my_iter=iter(my_range)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))#throws exception
'''RANGE SLICING
        we can slice ranges like lists and other objects.
'''
range(0,5)[2:4]
range(0,5)[4:2:-1]
#COMPARING RANGES
range(0)==range(4,2)
