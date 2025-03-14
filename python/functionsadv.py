'''---------------------------FORCED KEYWORD ARGUMENTS----------------------------
        *ADVANTAGES OF KEYWORD ARGUMENTS:
            :.not forced to a particular order in which you supply your arguments
            :.they provide clarity.
        #to force keywords we use '*'.
'''
def f(*,a,b):
    print(a,b)
#f(1,2)#would give error
#f(a=1,b=2)#would run

'''some functions require a long list of arguments.
To achieve this we use a dictionary with all the named arguments and pass that to the function.
        We can unpack the dict with named keywords using the prefix '**'.
'''
args={"a":1,"b":2}
f(**args)
#Similarly we can use a list and a single * to unpack it.
'''--------------DECORATORS--------------------------'''
'''These are wrappers around a function that modify the behaviour of the function in a certain way.'''
def print_argument(func):
    def wrapper(the_number):
        print("Argument for",func.__name__,"is",the_number)
        return func(the_number)
    return wrapper
@print_argument#decorator
def add_one(x):
    return x+1
print(add_one(1))
'''---------------------ANONYMOUS FUNCTIONS---------------------
        Used when we don't want to name a function.
        :.Lambda function.
'''
numbers=[1,2,3,4]
times_two=map(lambda x:x*2,numbers)
list(times_two)
