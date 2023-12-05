

import aocd

raw = aocd.get_data(day=15, year=2022)

raw = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''
raw = aocd.get_data(day=15, year=2022)

data = raw.splitlines()

#print(data)


magic_row = 2000000
#magic_row = 10


info = []

# [0] = sensor x
# [1] = sensor y
# [2] = dist (sensor to beacon)
# [3] = y dist (beacon to magic)
# [4] = beacon x
# [5] = beacon y

for d in data:
    sens = [0,0,0,0,0,0]
    ds = d.split('=')
    #print(ds)

    dsx = ds[1].split(',')
    sens[0] = int(dsx[0])
    dsy = ds[2].split(':')    
    sens[1] = int(dsy[0])
    dbx = int(ds[3].split(',')[0])
    dby = int(ds[4])

    sens[2] = abs(sens[0]-dbx)+abs(sens[1]-dby)
    sens[3] = abs(sens[1]-magic_row)
    sens[4] = dbx
    sens[5] = dby
    info.append(sens)

#print(info)

minx = magic_row
for s in info:
    nx = s[0]-s[2]
    if minx > nx:
        minx = nx-10
maxx = magic_row
for s in info:
    nx = s[0]+s[2]
    if maxx < nx:
        maxx = nx+10
minx=0
maxx=0
print(f'Min={minx} and Max={maxx}')
cnt = 0
y = magic_row
for x in range(minx,maxx):
    close = False
    isBeacon = False
    #print(f'x = {x}')
    for s in info:
        #print(f"X={x} vs {s[4]}  Y={y} vs {s[5]}")
        if (s[4] == x) and (s[5] == y):
            isBeacon = True
            break
    if not isBeacon:
        for s in info:
            #d = abs(s[0]-x)+abs(s[1]-y)
            d = abs(s[0]-x)+s[3]
            if d <= s[2]:
                close = True
                #xs.append(x)
                break
        if close:
            cnt += 1

print(f'Count = {cnt}')
print(f'4582667 right')

import time
minx = 0
maxx = 4000001
miny = 0
maxy = 4000001
sx = 0
sy = 0
start = time.time()
for x in range(minx,maxx):
    if x%10 == 0:
        end = time.time()
        print(f'X={x} - DT={end - start}')
        start = end
    for y in range(miny,maxy):
        found = False
        for s in info:
            if abs(s[0]-x) < s[2]:
                found = True
                break
            if abs(s[1]-y) < s[2]:
                found = True
                break
            if (abs(s[0]-x)+abs(s[1]-y)) < s[2]:
                found = True
                break
        if not found:
            print(f'x={x}, y={y}')
            sx = x
            sy = y
            print(f'Freq = {sx*4000000+sy}')
