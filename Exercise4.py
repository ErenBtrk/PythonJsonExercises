'''
4. Write a Python program to convert Python dictionary object 
(sort by key) to JSON data. Print the object members with indent level 4. 

'''

import json

python_dict= {"firstName" : "ali",
              "lastName" : "veli",
              "age" : "1993",
              "languages" : ["english","turkish"]
            }

json_obj = json.dumps(python_dict,sort_keys=True,indent = 4)
print(json_obj)

with open("jsondata.json","w") as file:
    file.write(json_obj)