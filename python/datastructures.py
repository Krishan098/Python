if isinstance(2,int):
    print('int')

class datatype():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pass
    def isequal(self):
        if self.x==self.y:
            print("They are same")
        else:
            print("not same")
q=datatype(10,15)
z=datatype(10,10)
q.isequal()
z.isequal()

from decimal import *
#getcontext().power=6
Decimal(6)/Decimal(7)


'''
---------------Tuples-----------------------'''
#sequence data type(list, range, tuple)
'''
    :. can hold multiple values in a single variable.
    :. it's ordered.
    :.can have duplicate values.
    :.indexed
    :.can have arbitrary length
    :.immutable
    :.defined using ()
    :. it can be hashed and can be a key in a dictionary.
    
'''

num=(1,2,4)
same=1,2,4
string=('HEllo','world')
mixed=('hello',1,2,True,3./4,)
print(tuple([0,1,2]))

l1=[1,2,3,]
l2=[4,5,6,]
t=(*l1,*l2)
#print(t)
#the * operator unpacks the lists into individual elements
#print(*t)
''' 
    Another way to unpack tuples.
    :. Multiple Assignment
    :.Works for strings and lists too
'''
person=('erik',38,True)
name,age,registered=person
#print(name)
len(t)
'''
    A tuple can have duplicates while a set can't.
'''
'''
----------------------LIST-----------------------
'''
listp=[1,'erik',[1,2,4,],{'age':39}]
#print(*list)
#print(tuple(range(1,5)))
#Nested lists
k=(listp[2][1])
listp.append('a')
list0=[2,4,5,]
list1=list0+listp
print(list1)
list1.extend(listp)
list1.pop(4)
del list1[0]
#del can delete any object in python
'''
    Remove removes the first occurence of the given object in a list.
'''
list1.remove(1)
list1.clear()#removes all elements from the list
'''
    REMOVING DUPLICATES: no specific way
    A set can contain no duplicates
    so convert list to set first and then back to list
'''
#list(set(listp))
my_list=[1,2,3,4,2,2,5]
#print(list(set(my_list)))
listp[0]=400
len(listp)
listp.count(400)
listp.index(400)
#the index method takes 2 optional parameters: start and stop.
for n in list0:
    print (n)
listp.__str__()
'''
    Sorted function and sort method
'''
#listp.sort()
list0.sort(reverse=True)
sorted(list1)
sorted(my_list,reverse=True)
'''Slicing'''
my_list[0:5:2]#[start:stop:step] stop is exclusive
'''Reversing:
        :.in-place reverse method
        :.list slicing with a negative step size results in a new list.
        :.create a reverse iterator, with the reversed() function.
'''
my_list.reverse()
my_list2=my_list[::-1]
rev=reversed(my_list)
#print(rev)
print(list(rev))
'''-----------------------------------SET-----------------------------
            :. collection of distinct elements.
            :.unordered
'''
mix_set={1,'a',91,(2,1)}
mix_set.add(4)
mix_set.update(range(3))#use update if multiple elements are to be added
p={x for x in 'hi my name is alphonso' if x not in '., '}
print(p)
''' Used for mathematical operations
        :.difference
        :.Union
        :. Intersection
        :.Subsets and supersets
'''
a={1,2,3,4,5,}
b={3,4,5,6,7,}
print(a-b)
print(b-a)
print(a^b)#symmetric difference
print(a&b)#intersection
A={1,2,3}
B={1,2,3,4,5}
C={1,2,3,10}
print(A<B)#is A subset of B
print(B>A)#is B superset of A
print(A|B)#Union
'''Frozenset:Unlike the usual mutual set, this one gets frozen directly after creation
:.WE CAN MIX THE SET AND THE FROZENSET TYPES.   
:. All operations work on these combinations.
:. Frozen set is hashable
:.A.union(B),A.intersection(B),A.difference(B)
'''
''' 
-------------------------------DICTIONARY---------------------------------------
'''
#syntax of a JSON document

numbers={'jack':'0888289922','Pete':'8973677637'}
numbers['Pete']
del(numbers['jack'])

print(numbers.get('L',8887788))
print(numbers)
numbers['Pete']='12345678'

a={'sub_dict':{'b':True},'mylist':[100,200,399]}
a['sub_dict']['b']
a['mylist'][0]
dict([ ('Jack', '070-02222748'), 
           ('Pete', '010-2488634'), 
           ('Eric', '06-10101010') ])
{x : x**2 for x in (2,4,6)}
c=['B','A','C']
k=dict.fromkeys(c,(b,a,c))
#print(k)
import json
jsonstring='{"name":"erik","age":38,"married":true}'
json.loads(jsonstring)
'Jack' in numbers
#Value in view object change as the content of the dictionary changes.
numbers.values()
numbers.keys()
'''items method return an iterable view object, offering both the keys and values'''
numbers.items()
for name,phonenr in numbers.items():
    print(name,":",phonenr)
#To access keys
list(numbers)
sorted(numbers)
'''Merging Dicts'''
n=numbers| k
merged={**numbers,**k}
