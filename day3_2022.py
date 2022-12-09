import aocd




raw = aocd.get_data(day=3, year=2022)
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

def score_letter(l):
    if l.isupper():
        return ord(l)-ord('A')+27
    else:
        return ord(l)-ord('a')+1

score = 0
    
for d in data:
    assert(len(d)%2 == 0)
    f = d[0:len(d)//2]
    l = d[len(d)//2:]
    fs = {*f}
    ls = {*l}
    
    # check character overlap
    sol = fs.intersection(ls)
    
    assert(len(sol) == 1)
    #print(f'Let = {list(sol)[0]} and value = {score_letter(list(sol)[0])}')
    score += score_letter(list(sol)[0])

print(score)

score = 0
i = 0
groups = len(data)//3
for i in range(0,groups):
    a = {*data[i*3]}
    b = {*data[i*3 + 1]}
    c = {*data[i*3 + 2]}

    sol = a.intersection(b,c)
    assert(len(sol) == 1)
    print(f'Let = {list(sol)[0]} and value = {score_letter(list(sol)[0])}')
    score += score_letter(list(sol)[0])

print(score)

