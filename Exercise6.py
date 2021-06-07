'''
6. Write a Python program to create a new JSON file from an existing JSON file.

'''

import json

with open("jsondata.json","r") as file:
    data = json.load(file)

with open("newjsondata.json","w") as file:
    json.dump(data,file)

