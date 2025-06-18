import random as rand
import string

dicts=[]
for i in range(rand.randint(2,10)):
    num_keys=rand.randint(2,10)
    keys = rand.sample(string.ascii_lowercase,num_keys )
    values = [rand.randint(0, 100) for _ in range(num_keys)]
    dicts.append(dict(zip(keys, values)))

print(dicts)

