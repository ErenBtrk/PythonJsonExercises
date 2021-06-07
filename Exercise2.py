'''
2. Write a Python program to convert Python object to JSON data.

'''

import json

python_obj = {"name" : "ali",
              "class" : "12",
              "age"  : "17"}

json_obj = json.dumps(python_obj)

print(json_obj)
print(type(json_obj))

