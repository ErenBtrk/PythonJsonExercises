'''
1. Write a Python program to convert JSON data to Python object. 

'''

import json

json_obj =  '{ "Name":"Ali", "Class":"12", "Age":17 }'

python_obj = json.loads(json_obj)
print(type(python_obj))

for key,value in python_obj.items():
    print(f"{key} = {value}")