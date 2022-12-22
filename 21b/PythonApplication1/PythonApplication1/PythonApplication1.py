import re
from sympy import symbols, solve

monkeys = {}
with open("input.txt", "r") as fContent:
    for line in fContent.readlines():
        monkeys[line[:4]] = line[6:].strip()

def createEquation(key):
    if key == "humn": return "humn"
    keys = re.findall(r"[a-z]+", monkeys[key])
    if len(keys) > 0:
        return f"({createEquation(keys[0])} {monkeys[key][5:6]} {createEquation(keys[1])})"
    return f"{monkeys[key]}"
    
def getValue(key, sValue):
    if not monkeys[key].isdigit():
        v = monkeys[key]
        keys = re.findall(r"[a-z]+", v)

        fValue = getValue(keys[0])
        sValue = getValue(keys[1])
        
        v = v.replace(keys[0], fValue).replace(keys[1], sValue)
        return str(int(eval(v)))
    else:
        return monkeys[key]

rootKeys = re.findall(r"[a-z]+", monkeys["root"])

sEquation = eval(createEquation(rootKeys[1]))
fEquation = createEquation(rootKeys[0])

humn = symbols("humn")
expr = (f"{fEquation} - {sEquation}")
s = solve(expr)

print(f"Number to yell: {s}")