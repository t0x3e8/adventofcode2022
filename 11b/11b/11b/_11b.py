import re, time, math
from collections import deque

def add(a, b): return a + b
def multiply(a, b): return a * b

fContent = open("input.txt", "r").read()
monkeys = {}

mSet = [re.findall(r"Starting items: (.*)", fContent),
           re.findall(r"Operation: new = (.*)", fContent), 
           re.findall(r"Test: divisible by (.*)", fContent),
           re.findall(r"If true: throw to monkey (.*)", fContent),
           re.findall(r"If false: throw to monkey (.*)", fContent)]

for i in range(len(mSet[0])):
    monkeys[str(i)] = {"items": deque(re.findall(r"\d+", mSet[0][i])),
               "op": mSet[1][i],
               "test": int(re.findall(r"\d+", mSet[2][i])[0]),
               "true": int(re.findall(r"\d+", mSet[3][i])[0]),
               "false":  int(re.findall(r"\d+", mSet[4][i])[0]),
               "count": 0}
          
M = math.prod(int (x) for x in mSet[2])
start_time = time.time()
for r in range(10000):
    for k, v in monkeys.items():
        while len(v["items"]) > 0:
            item = v["items"].pop()
            v["count"] += 1
            #wl = eval(v["op"].replace("old", str(item)))
            
            args = v["op"].split(" ")
            args[0] = int(item) if args[0] == "old" else int(args[0])
            args[2] = int(item) if args[2] == "old" else int(args[2])
            wl = int()
            if "*" == args[1]:
                wl = multiply(args[0], args[2])
            elif "+" == args[1]:
                wl = add(args[0], args[2])

            wl = wl % M
            test = wl % (v["test"]) == 0
            if test:
                monkeys[str(v["true"])]["items"].append(wl)
            else:
                monkeys[str(v["false"])]["items"].append(wl)

end_time = time.time()
elapsed_time = end_time - start_time
print('The operation took {} seconds to complete.'.format(elapsed_time))

for k, v in monkeys.items():
    print(f"Monkey {k} inspected items {v['count']} times.")

list = list(sorted(monkeys.items(), key = lambda x: x[1]["count"], reverse=1)[:2])
print(f"Tatal is {list[0][1]['count']} * {list[1][1]['count']} = {list[0][1]['count'] * list[1][1]['count']}")   
    