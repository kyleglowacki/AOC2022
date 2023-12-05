stone = '#'
sand = 'o'
air = ' '

def make_grid(x,y, d = 0):
    grid = []
    for i in range(y):
        g = [d] * x
        grid.append(g)
    return grid

def open(grid, pt):
    global air
    return grid[pt[1]][pt[0]] == air

def mark(grid, pt, val):
    #print(pt)
    grid[pt[1]][pt[0]] = val
    return grid

def mk_pt(pt_str):
    pt = pt_str.split(',')
    pt[0] = int(pt[0])
    pt[1] = int(pt[1])
    return pt
    
def process_line(d, g, f):
    corners = d.split(' -> ')
    last = mk_pt(corners[0])
    g = mark(g,last,stone)
    for c in corners:
        cur = mk_pt(c)
        # loop from last to cur and mark them all
        for y in range(min(last[1],cur[1]), max(last[1],cur[1])+1):
            g = mark(g, [last[0],y], stone)
            if y > f:
                f = y+2
        for x in range(min(last[0],cur[0]), max(last[0],cur[0])+1):
            g = mark(g, [x,last[1]], stone)
                
        last = cur

    return g, f

def add_sand(x,y,g):
    global air
    global sand

    if g[y][x] == sand:
        return g, True
    
    stuck = False
    # While not stuck
    #     sand falls
    #     sand rolls left/right
    while not stuck:
        #print(f'Checking {x},{y+1} {grid[y+1][x]}')
        if grid[y+1][x] != air:
            if grid[y+1][x+1] != air and grid[y+1][x-1] != air:
                stuck = True
                print(f"Placing Sand at {x},{y}")
                grid[y][x] = sand
                return g, False
            else:
                # roll left
                if grid[y+1][x-1] == air:
                    #print(f'Rolling left {x-1},{y+1}')
                    return add_sand(x-1,y+1,g)
                else:
                    #print(f'Rolling right {x+1},{y+1}')
                    return add_sand(x+1,y+1,g)
        elif y == 998:
            print(f'Fell off {x}')
            return g, True            
        else:
            y += 1

    return g, False

def printgrid(g, xl,xu,yl,yu):
    for y in range(xl,xu):
        for x in range(yl,yu):
            print(g[y][x],end='')
        print("")
    print("")
import aocd
raw = aocd.get_data(day=14, year=2022)
data = raw.splitlines()
#data=['498,4 -> 498,6 -> 496,6','503,4 -> 502,4 -> 502,9 -> 494,9']
#print(data)

max_x = 4000
grid = make_grid(max_x, 1000,' ')

floor = 1
for d in data:
    grid,floor = process_line(d, grid, floor)

print(f"Floor is at {floor}")
for x in range(max_x):
    grid = mark(grid, [x,floor], stone)

# Now add sand...
done = False
cnt = 0
while not done:
    
    grid, done = add_sand(500,0, grid)
    if not done:
        cnt += 1
    #printgrid(grid, 10,20,490,510)

print(f"Dropped {cnt} pieces of sand")
