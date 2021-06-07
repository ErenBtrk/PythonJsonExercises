'''
5. Write a Python program to convert JSON encoded data into Python objects.

'''

import json

with open("jsondata.json","r") as file:
    dict1 = json.load(file)

python_obj = json.loads(dict1)


print(python_obj)
print(type(python_obj))