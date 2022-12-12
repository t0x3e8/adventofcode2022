import re, time
import re, time
from collections import deque

fContent = open("testinput.txt", "r").read()
monkeys = {}

mSet = [re.findall(r"Starting items: (.*)", fContent),
           re.findall(r"Operation: new = (.*)", fContent), 
           re.findall(r"Test: divisible by (.*)", fContent),
           re.findall(r"If true: throw to monkey (.*)", fContent),
           re.findall(r"If false: throw to monkey (.*)", fContent)]

monkeys = {
    "0": {"items": deque(re.findall(r"\d+", mSet[0][0])),
           "op": mSet[1][0],
           "test": int(re.findall(r"\d+", mSet[2][0])[0]),
           "true": int(re.findall(r"\d+", mSet[3][0])[0]),
           "false":  int(re.findall(r"\d+", mSet[4][0])[0]),
           "count": 0},
    "1": {"items": deque(re.findall(r"\d+", mSet[0][1])),
           "op": mSet[1][1],
           "test": int(re.findall(r"\d+", mSet[2][1])[0]),
           "true": int(re.findall(r"\d+", mSet[3][1])[0]),
           "false":  int(re.findall(r"\d+", mSet[4][1])[0]),
           "count": 0},
    "2": {"items": deque(re.findall(r"\d+", mSet[0][2])),
           "op": mSet[1][2],
           "test": int(re.findall(r"\d+", mSet[2][2])[0]),
           "true": int(re.findall(r"\d+", mSet[3][2])[0]),
           "false":  int(re.findall(r"\d+", mSet[4][2])[0]),
           "count": 0},
    "3": {"items": deque(re.findall(r"\d+", mSet[0][3])),
           "op": mSet[1][3],
           "test": int(re.findall(r"\d+", mSet[2][3])[0]),
           "true": re.findall(r"\d+", mSet[3][3])[0],
           "false":  re.findall(r"\d+", mSet[4][3])[0],
           "count": 0},
            }

start_time = time.time()
for r in range(400):
    for k, v in monkeys.items():
        while len(v["items"]) > 0:
            item = v["items"].pop()
            v["count"] += 1
            wl = eval(v["op"].replace("old", str(item)))
            test = wl % v["test"] == 0
            if test:
                monkeys[str(v["true"])]["items"].append(wl)
            else:
                monkeys[str(v["false"])]["items"].append(wl)

end_time = time.time()
elapsed_time = end_time - start_time
print('The operation took {} seconds to complete.'.format(elapsed_time))
           
for k, v in monkeys.items():
    print(f"Monkey {k} inspected items {v['count']} times.")
    