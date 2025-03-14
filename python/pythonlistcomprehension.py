'''---------------LIST COMPREHENSION-------------------------
            A python list comprehension is a language construct.            
            Used to create a python list based on an existing list.
            :.Basic syntax:
                [<expression> for item in list if <conditional>]
'''
#if-part is optional
#we do need a list to start from, or anything that can be iterated
#range() is a special type of iterator called a generator.
[x for x in range(1,5)]
[x for x in range(1,10) if x%2==0]
#if acts as a filter.
[x+4 for x in [10,20]]
def some_func(a):
    return (a+5)/2
m=[some_func(x) for x in range(8)]
'''---------------NESTED LIST COMPREHENSIONS--------------'''
m=[[j for j in range(3)] for i in range(4)]
[value for sublist in m for value in sublist]
'''---------------------------SET COMPREHENSIONS------------------'''
{s for s in range(1,5) if s%2}
'''----------------------DICTIONARY COMPREHENSIONS---------------------'''
{x:x**2 for x in (2,4,6)}