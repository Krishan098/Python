'''------------------------PYTHON ITERATOR-------------------------------
        :.Iterator:An object that can be iterated, meaning we can keep asking it for a new element untiil there are no elements left.
                Elements are requested using a method called __next__.
                
        :.Iterable: An objecr that implements another special method, called __iter__.This returns an iterator.
        
        Iterator implements a func that needs to carry the exact name __next__.
        When no more elements are left to be returned ,it throws an exception- StopIteration.
        
        For an iterator object, we need to first call the __iter__ method on an iterable object.
'''
my_iterable=range(1,3)
my_iterator=my_iterable.__iter__()
my_iterator.__next__()
my_iterator.__next__()
#my_iterator.__next__()
#special type of iterators--> generators: range()

class EvenNumbers:
    last=0
    def __iter__(self):
        return self
    def __next__(self):
        self.last+=2

        if self.last>8:
            raise StopIteration
        return self.last
evennumbers=EvenNumbers()
for num in evennumbers:
    print(num)