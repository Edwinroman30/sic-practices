accounts = {
    "do": {
        "mario" : ["mrio", "asdaw", 30, 399.02],
        "juan" : ["juasd", "asdaw", 30, 399.02],
        "antonio": ["anuri", "asdaw", 30, 399.02],
    },
    "co": {
        "franco" : ["farnaco", "asdaw", 30, 399.02],
        "pedro" : ["droper", "asdaw", 30, 399.02],
        "lipa": ["dua", "asdaw", 30, 399.02],
    }
}

all_users = []

'''
for keys, values in accounts.items():
    for _, val in values.items():
        all_users.append(val)

for val in all_users:
    if(val[0] == "dua"):
        print(val)  
 '''
from collections import defaultdict


k = ('a','b','c','d')
mydic = dict.fromkeys(k)

''' print(mydic.get("z",0))
print(mydic) '''

print(accounts["do"].get("mari"))
print(accounts.get("do")["marimo"])