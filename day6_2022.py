import aocd




raw = aocd.get_data(day=6, year=2022)
# '127\n147\n148\n147\n146\n153\n ... '
data = raw
#data = raw.splitlines()
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

#off = 4
off = 14

# TODO End?
for i in range(0,len(data)-off):
    s = set(data[i:i+off])
    if len(s) == off:
        print(f'Index = {i+off}')
        print(f'Data  = {data[i:i+off]}')
        break

