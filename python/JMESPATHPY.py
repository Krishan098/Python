#JMESPath is a JSON query language. JMESPath in python allows you to obtain the data you need from a JSON doc or dict.
{
    "persons":{
        "name":"erik",
        "age":"38"
    }
}
persons={
  "persons": [
    { "name": "erik", "age": 38 },
    { "name": "john", "age": 45 },
    { "name": "rob", "age": 14 }
  ]
}
#To extract info from this array, we could apply a for loop but that leads to complexity.
import jmespath
j={"people":[{"name":"erik","age":38}]}
jmespath.search("people[*].age",j)
jmespath.search('persons[0]',persons)
jmespath.search('persons[*].age',persons)
jmespath.search("persons[?name=='erik'].age",persons)