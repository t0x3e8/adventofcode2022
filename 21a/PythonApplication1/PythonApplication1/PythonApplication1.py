import re

monkeys = {}
with open("input.txt", "r") as fContent:
    for line in fContent.readlines():
        monkeys[line[:4]] = line[6:].strip()
        
def getValue(key):
    if not monkeys[key].isdigit():
        v = monkeys[key]
        fKey = re.findall(r"[a-z]+", v)[0]
        sKey = re.findall(r"[a-z]+", v)[1]
        fValue = getValue(fKey)
        sValue = getValue(sKey)
        v = v.replace(fKey, fValue).replace(sKey, sValue)
        return str(eval(v))
    else:
        return monkeys[key]
    
value = getValue("root")
print(value)
