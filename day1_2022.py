import aocd




raw = aocd.get_data(day=1, year=2022)
# '127\n147\n148\n147\n146\n153\n ... '

data = raw.splitlines()
# ['127', '147', '148', ... ]

# convert to int
#data= [int(x) for x in data]

print(data)

# One way
#z = [1 for x in range(len(data)-1) if data[x+1] > data[x]]
#print(len(z))

# generates T/F array.. sum seems to count True
#z = [data[x+1] > data[x] for x in range(len(data)-1)]
#print(sum(z))
e=[]
i = 0
e.append(0)
for d in data:
    if d != '':
        e[i] += int(d)
    else:
        e.append(0)
        i += 1

print(e)

ee = e
total = 0
total += max(ee)
ee[ee.index(max(ee))] = 0

total += max(ee)
ee[ee.index(max(ee))] = 0

total += max(ee)
ee[ee.index(max(ee))] = 0

print(total)
