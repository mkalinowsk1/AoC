import json

def sumObject(obj):
    if type(obj) is int:
        return obj
    
    if type(obj) is list:
        return sum(map(sumObject, obj))
    
    if type(obj) is dict:
        vals = obj.values()
        
        #remove these two lines for part one
        if "red" in vals:
            return 0
        
        return sum(map(sumObject, vals))
    
    else:
        return 0


with open("input.in") as f:
    obj = json.loads(f.read())
    print(sumObject(obj))