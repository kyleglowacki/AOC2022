def dist(h,t):
    x = abs(h[0] - t[0])
    y = abs(h[1] - t[1])
    return max(x,y)
    
def move_x(h,t):
    if h[0] < t[0]:
        t[0] -= 1
    else:
        t[0] += 1    
    return t

def move_y(h,t):
    if h[1] < t[1]:
        t[1] -= 1
    else:
        t[1] += 1
    return t
        
def move_tail(h,t):
    if dist(t,h) < 2:
        return t    
    if h[0] == t[0]:
        t = move_y(h,t)
    elif h[1] == t[1]:
        t = move_x(h,t)
    else:
        t = move_x(h,t)
        t = move_y(h,t)
    return t

def move_tails(g,rope):
    for j in range(1,rope_len):
        rope[j] = move_tail(rope[j-1],rope[j])
    g[rope[rope_len-1][0]][rope[rope_len-1][1]] = 1
    return g, rope

displacement = {"L":[-1,0], "R":[1,0], "U":[0,-1], "D":[0,1]}

def move(g, r, d, dir):
    for i in range(0,d):
        # move head
        r[0][0] += displacement[dir][0]
        r[0][1] += displacement[dir][1]
        g,r = move_tails(g,r) 
    return g, r

import aocd
raw = aocd.get_data(day=9, year=2022)

data = raw.splitlines()
# ['127', '147', '148', ... ]

#print(data)

w = 1000
h = 1000

# x,y
grid = [0] * h
for y in range(0,h):
    grid[y] = [0]*w

# Guess on grid
rope_len = 10
rope = []
for _ in range(rope_len):
    rope.append([500,500])

for d in data:
    dir,dis = d.split(' ')
    dis = int(dis)
    grid,rope = move(grid, rope, dis, dir)

sum = 0
for col in grid:
    for ele in col:
        sum += ele

print(sum)
