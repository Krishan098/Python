'''JSON- Javascript object notation. '''
import json
#json.loads(...)- load string
'''
        converts:
            :. objects to dictionaries
            :. arrays to lists
            :. booleans ,integers, floats and strings are recognised for what they are and will be converted into the correct types in Python
            :. Any null will be converted into Python's None type
'''
jsonstring='{"name":"erik","age":38,"married":true}'
person=json.loads(jsonstring)
print(person['name'],'is',person['age'],'years old')
print(person)
'''Encoding with json.dumps'''#dump to string
case1={'name':'erik','age':'38','married':True}
json_string=json.dumps(case1)
print(json_string)
print(type(json_string))

print(json.dumps(case1,indent=2))
#json.load'''to load data from a file'''
    # with open('data.json') as json_file:
    #     data= json.load(json_file)
'''json.dump is used to write data to a json file'''
data={'name':'Eric','age':38}
with open('data.json','w') as json_file:
    json.dump(data,json_file)
    
'''JSON5 is an extension of JSON:
                Allows for more human-readable and editable JSON files. Notable JSON5 features are:
                        :. single-line and multi-line comments
                        :. trailing commas in objects and arrays
                        :. single-quoted strings
   
   PyJSON5: a library that uses the official JSON5 C library, making it the fastest option to use.
   json5: a pure Python implementation
   
'''
import pyjson5 as json5
with open("data.json") as f:
    p=json5.decode(f.read())
print(p)