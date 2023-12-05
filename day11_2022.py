class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ''
        self.divisibility_test = 1
        self.f = 0
        self.t = 0
        self.insp_cnt = 0

def parse(d):

    m = Monkey()
    l = d[1].split(':')[1].split(', ')
    for package in l:
        m.items.append(int(package))
    tmp = d[2].split(':')[1][1:]
    m.operation = tmp[6:]
    m.divisibility_test = int(d[3].split()[3])
    m.t = int(d[4].split()[5])
    m.f = int(d[5].split()[5])
    return m

def divisible_by(x, y):
    return (x % y) == 0

def rw(val,worry):
    # I hope this is mathematically correct
    if val > 9699690:
        #print(f'{val} reduced to {val%9699690}')
        val = val % 9699690
    return val//worry
    
def tosser(idx,ms, worry):
    m = ms[idx]
    for i in m.items:
        m.insp_cnt += 1
        old = i
        new = eval(m.operation)
        new = rw(new,worry)
        if divisible_by(new, m.divisibility_test):
            ms[m.t].items.append(new)
        else:
            ms[m.f].items.append(new)
    return ms


import aocd
raw = aocd.get_data(day=11, year=2022)
data = raw.splitlines()

ms = []
for i in range(8):
    ms.append(parse(data[i*7:i*7+7]))

# Part 1
#rnds = 20
#w = 3

# Part 2
rnds = 10000
w = 1

for rnd in range(1,rnds+1):
    if divisible_by(rnd,100):
        print(f'{rnd}')
    for i in range(8):
        ms = tosser(i,ms,w)
        ms[i].items = []

insp = []
for i in range(8):
    insp.append(ms[i].insp_cnt)

insp.sort()
print(insp)
print(insp[6] * insp[7])
