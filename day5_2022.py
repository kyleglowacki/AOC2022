import aocd




raw = aocd.get_data(day=5, year=2022)
# '127\n147\n148\n147\n146\n153\n ... '

data = raw.splitlines()
# ['127', '147', '148', ... ]

#print(data)

ss = {1:[], 2:[], 3:[], 4:[], 5:[],6:[],7:[],8:[],9:[]}

for i in range(7,-1,-1):
    print(i)
    idx = 1
    for j in range(1,34,4):
        v = data[i][j]
        if v != ' ':
            assert(v != '[')
            assert(v != ']')
            assert(v != '')
            ss[idx].append(v)
        idx += 1
        
ss1 = ss
#print(ss1)

#for d in data:
#    w = []
#    w = d.split(' ')
#    if (len(w) == 6) and (w[0] == "move"):
#        w[1] = int(w[1])
#        w[3] = int(w[3])
#        w[5] = int(w[5])
#        for i in range(w[1]):
#            ss1[w[5]].append(ss1[w[3]].pop())
#
#print(ss1)

ss2 = ss



for d in data:
    w = []
    w = d.split(' ')
    if (len(w) == 6) and (w[0] == "move"):
        print(d)
        w[1] = int(w[1])
        w[3] = int(w[3])
        w[5] = int(w[5])
        temp = ''
        for i in range(w[1]):
            temp += ss2[w[3]].pop()
            print(f'Popped, temp now {temp}')
        for i in range(w[1]):
            ss2[w[5]].append(temp[-1])
            temp = temp[:-1]
            print(f'Appended, temp now {temp}')

print(ss2)

# convert to int
#data= [int(x) for x in data]


# One way
#z = [1 for x in range(len(data)-1) if data[x+1] > data[x]]
#print(len(z))

# generates T/F array.. sum seems to count True
#z = [data[x+1] > data[x] for x in range(len(data)-1)]
#print(sum(z))

