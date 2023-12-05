import aocd




raw = aocd.get_data(day=10, year=2022)
data = raw.splitlines()


cyc = [20,60,100,140,180,220]

# index by cycle
signals=[]
X = 1
signals.append(X) #cycle zero to make the 20,60,etc line up 

def l():
    global signals
    return len(signals)-1

for d in data:
    # Either way append (for noop or first cycle of addx)
    signals.append(X)
    print(f'Cycle {l()} value is {signals[l()]}')
    vals = d.split(' ')
    if vals[0] == 'addx':
        signals.append(X)
        X += int(vals[1])
        print(f'Cycle {l()} value is {signals[l()]}')

        
#print(signals)
        
sums = 0
for c in cyc:
    print(f'Sum {c} times {signals[c]}')
    sums += (signals[c] * c)
    
print(sums)

def draw(ri,i):
    global signals
    cycle = ri*40+i+1
    print(f"Look at {i}, cycle {cycle} when signal is {signals[cycle]}")
    # i is pixel position to draw

    # eg i = 2, signal = 1, then draw.  Signal is middle of sprite
    # ...
    # . 
    if signals[cycle] == i-1:
        return True
    if signals[cycle] == i:
        return True
    if signals[cycle] == i+1:
        return True
    return False


rows = []
ans = []
for _ in range(6):
    rows.append('.' * 40)
print(rows[0])
    
ri =  0
for r in rows:
    r = '.' * 40
    for i in range(40):
        if draw(ri,i):
            print("Update pixel")
            r = r[:i] + '#' + r[i+1:]
    ans.append(r)
    ri += 1



for r in ans:
    print(r)
