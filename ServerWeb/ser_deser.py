
import ast, sys

"""
mylist_1 = "['mario', 'gino','lucrezia']"

mylist_2 = ['mario', 'gino','lucrezia']

def Serializza(mylist_1: list) -> str:
    return (str(mylist_1))

def Deserealizza(mylist_2: str) -> list:
    mylist_2 = ast.literal_eval(mylist_2)

    return mylist_2

"""

import json


# MODO 1

def Serialjson1(dData, file_path) -> bool:
        sData = json.dump(dData)
        try:
            with open(file_path, "w") as ser_deser: # nome del mio file
                ser_deser.write(sData)
            return True
        except:
             return False
        

# MODO 2

def Serialjson2(dData, file_path) -> bool:
        try:
            with open(file_path, "w") as ser_deser: # nome del mio file
                json.dumps(dData, ser_deser)
            return True
        except:
             return False
        

mydict_1 = { "brand": "Ford",
"electric": False,
"year": 1964,
"colors": ["red", "white", "blue"]}

mydict_2 = "{ 'brand':   'Ford'," + \
"'electric': False," + \
"'year': 1964," + \
"'colors': ['red', 'white', 'blue']}"


bRet = Serialjson1(mydict_1,"./prodotto.json")
print(bRet)
sys.exit


# MODO 1

def Deserialjson1(file_path: str) -> dict:
    sData = ""
    sAppo = ""
    dData = {}
    try:
        with open(file_path, "r") as ser_deser:
            sAppo = ser_deser.read(500)
            while len(sAppo) == 500:
                sData += sAppo
                sAppo = ser_deser.read(500)
            if len(sAppo) > 0:
                sData += sAppo
        if len(sData) > 0:
            json.loads(sData)
            return dData
        else:
            return None
    except:
        return None
         
           





    
