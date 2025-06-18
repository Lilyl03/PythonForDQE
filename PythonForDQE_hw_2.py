import random as rand
import string

"""
1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

"""

dicts=[]
for i in range(rand.randint(2,10)):
    num_keys=rand.randint(2,10)
    keys = rand.sample(string.ascii_lowercase,num_keys )
    values = [rand.randint(0, 100) for _ in range(num_keys)]
    dicts.append(dict(zip(keys, values)))

print(dicts)


common_dict = {}

for dict_num, d in enumerate(dicts, start=1):
    for key, value in d.items():
        if key in common_dict:
            if value > common_dict[key][0]:
                common_dict[key] = (value, dict_num)
        else:
            common_dict[key] = (value, None)


final_dict = {f"{key}_{dict_num}" if dict_num else key: value for key, (value, dict_num) in common_dict.items()}

print(final_dict)
