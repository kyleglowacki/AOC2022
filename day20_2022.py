import aocd

raw = aocd.get_data(day=20, year=2022)
data = raw.splitlines()
try:
    d2 = [int(x) for x in data]
except:
    print(len(d2))

print(data)

d3 = [int(x) for x in data]

import numpy as np

print(len(d3))
print(len(np.unique(d3)))

# not unique... so how to find the instance of the number we need to move



# find zero
# index + 1000
# index + 2000
# index + 3000
