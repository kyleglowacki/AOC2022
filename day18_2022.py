import aocd


def printgrid(g, xl,xu,yl,yu):
    for y in range(xl,xu):
        for x in range(yl,yu):
            print(g[y][x],end='')
        print("")
    print("")


raw = aocd.get_data(day=18, year=2022)

data = raw.splitlines()

#print(data)

gm = 23
grid = []
for z in range(gm):
    ya = []
    for y in range(gm):
        x = [' ']*gm
        ya.append(x)
    grid.append(ya)

for d in data:
    x,y,z = d.split(',')
    x = int(x)+1
    y = int(y)+1
    z = int(z)+1
    grid[x][y][z] = 'X'

# grid marked, now count 'edges'

# check adjacent
def ca(x,y,z,v):
    global grid
    cnt = 0

    if grid[x+1][y][z] == v:
        cnt += 1
    if grid[x][y+1][z] == v:
        cnt += 1
    if grid[x][y][z+1] == v:
        cnt += 1
    if grid[x-1][y][z] == v:
        cnt += 1
    if grid[x][y-1][z] == v:
        cnt += 1
    if grid[x][y][z-1] == v:
        cnt += 1
    return cnt
def spread(x,y,z,v):
    global grid
    cnt = 0
    if grid[x+1][y][z] == v:
        grid[x+1][y][z] = 'W'
        cnt += 1
    if grid[x][y+1][z] == v:
        grid[x][y+1][z] = 'W'
        cnt += 1
    if grid[x][y][z+1] == v:
        grid[x][y][z+1] = 'W'
        cnt += 1
    if grid[x-1][y][z] == v:
        grid[x-1][y][z] = 'W'
        cnt += 1
    if grid[x][y-1][z] == v:
        grid[x][y-1][z] = 'W'
        cnt += 1
    if grid[x][y][z-1] == v:
        grid[x][y][z-1] = 'W'
        cnt += 1
    return cnt



total = 0
for d in data:
    x,y,z = d.split(',')
    x = int(x)+1
    y = int(y)+1
    z = int(z)+1
    total += ca(x,y,z,' ')
print(f'Total = {total}')
#for x in range(gm):
#    print(f"Layer {x}")
#    printgrid(grid[x],0,gm-1,0,gm-1)

grid[0][0][0] = 'W'
s = 1
while s != 0:
    s = 0
    for x in range(gm-1):
        for y in range(gm-1):
            for z in range(gm-1):
                if grid[x][y][z] == 'W':
                    s += spread(x,y,z,' ')
    print(f"Spread {s} times")

            
print("3222 too high")
print("2053 too low")
print("1337 too low")
total = 0
for d in data:
    x,y,z = d.split(',')
    x = int(x)+1
    y = int(y)+1
    z = int(z)+1
    total += ca(x,y,z,'W')
print(f'Total = {total}')


#for x in range(gm):
#    print(f"Layer {x}")
#    printgrid(grid[x],0,gm-1,0,gm-1)
