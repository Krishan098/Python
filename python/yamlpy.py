'''YAML-YAML ain't markup language, is a human-readable data serialization lang. 
        PyYAML:library
        It is easy to write and read for humans
            :. We can use comments
            :. we can store multiple documents in one YAML file with the ---separator.
            :. easy to read and parse
'''     
#YAML is perfect for congiguration files. 
#YAML is not part of the standard Python library unlike XML and JSON are.
import yaml
with open('config.yml','r') as file:
    prime_service = yaml.safe_load(file)
prime_service
prime_service['rest']['url']
#yaml.safe_load() to parse all kind of strings
names_yaml='''
    - 'eric'
    - 'justin'
    - 'mary-kate'
'''
names=yaml.safe_load(names_yaml)
names

'''Allows multiple documents in one file,separating them with a triple dash(---).
        USE the function yaml.safe_load_all() function.
        this function returns a generator that in turn will return all documents one by one.
        
'''
# with open('multi_doc.yml','r') as file:
#     docs=yaml.safe_load_all(file)
#     for doc in docs:
#         print(doc)

with open('names.yaml','w') as file:
    yaml.dump(names,file)
print(open('names.yaml').read())
#Converting YAML to JSON
import json
with open('names.yaml','r') as file:
    configuration=yaml.safe_load(file)
with open('config.json','w') as json_file:
    json.dump(configuration,json_file)
output=json.dumps(json.load(open('config.json'),indent=2))
print(output)
'''
    
'''