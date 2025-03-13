#!Exceptions-arise during a program's execution.
'''
    Exception class. they have their own descriptive names.
  
  
  Call STACK: It is an ordered list of functions that are currently being executed.
'''
try:
    print(2/0)
except ZeroDivisionError:
    print("can't divide by 0")

'''IOError: file is not there or permission is not there to access the file'''
try:
    with open("not.txt",'r') as f:
        f.write("Hello World!")
except IOError as e:
    print("An error occured :",e)
'''finally and else:
        finally block is executed even after an exception occurs. It is executed irrespective of an exception.
'''
try:
    f=open("myfile.txt",'w')
    f.write('Hello World!')
except IOError as e:
    print("An area occurred",e)
finally:
    print("Closing the file now")
    f.close()

'''
        Else block: This block executes only if no exception occurs.

'''
'''CREATE CUSTOM EXCEPTIONS:
        we can create a subclass of the Exception class.
'''
class UserNotFoundError(Exception):
    pass
'''
RAISING(OR THROWING) exceptions:
            we can raise exceptions using 'raise' keyword.
            fetch_user, that fetches some user data from an imaginary database.
'''
class UserNotFoundError(Exception):
    pass
def fetch_user(user_id):
    user=None
    if user==None:
        raise UserNotFoundError(f'USer {user_id} not in database')
    else:
        return user
users=[123,456,789]
for user_id in users:
    try:
        fetch_user(user_id)
    except UserNotFoundError as e:
        print("There was a error:",e)
#If you like to print the call stack : import traceback
import traceback
try:
    ...
except Exception:
    traceback.print_exc()