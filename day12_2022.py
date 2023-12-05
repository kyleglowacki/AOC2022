import aocd

raw = aocd.get_data(day=12, year=2022)
data = raw.splitlines()

width = len(data[0])
height = len(data)

# l r u d
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# on board
def valid(x, y):
    global width
    global height
    if x<0 or y < 0:
        return False
    if x>=width:
        return False
    if y>=height:
        return False
    return True

# Follow rules for up/down
def good_step(x,y,m,step):
    p = ord(m[step[1]][step[0]])
    n = ord(m[y][x])
    #print(f'Prev={p}, next={n}')
    # one step up
    if p+1 == n:
        #print("Step UP")
        return True, False
    # end!
    if m[y][x] == '{' and p >= ord('y'):
        #print("Step END")
        return True, True
    # step down
    if p >= n:
        #print("Step DOWN/Flat")
        return True, False
    return False, False

def mark_step(d, m, s, steps):
    cur = []
    done = False
    print(s)
    #print(steps)
    for step in steps[s-1]:
        for dir in dirs:
            nx = step[0]+dir[0]
            ny = step[1]+dir[1]
            #print(f"Consider {nx},{ny}")
            if valid(nx, ny):
                #print("Valid Step")
                good, done = good_step(nx,ny,m,step)
                if done:
                    steps.append(cur)
                    return d, done, steps
                if good:
                    #print("Good Step")
                    # not already used (avoid loops)
                    if d[ny][nx] == -1:
                        #print("Unused Step")
                        d[ny][nx] = s
                        cur.append([nx, ny])
    steps.append(cur)
    return d, done, steps

m = []
dist = []
for d in data:
    row = []
    z = []
    for l in d:
        row.append(l)
        z.append(-1)
    m.append(row)
    dist.append(z)

#initialize
start = m[20][0]
end = m[20][77]
m[20][0] = 'a'
m[20][77] = '{'
dist[20][0] = 0

# start loop
done = False
step = 0
steps = []
steps.append([[0, 20]])
while not done:
    step += 1
    dist, done, steps = mark_step(dist, m, step, steps)
    if step > 500:
        break

print(step)

r = 0
for row in dist:
    c = 0
    for ele in row:
        print('%3d%c' % (ele,m[r][c]), end='')
        c += 1
    print('')
    r += 1

###
### STEP 2
###

# reinit
m = []
dist = []
for d in data:
    row = []
    z = []
    for l in d:
        row.append(l)
        z.append(-1)
    m.append(row)
    dist.append(z)

#initialize all 'a' to be in initial steps

end = m[20][77]
m[20][0] = 'a'
steps = []
cur = []
r = 0
for row in m:
    c = 0
    for ele in row:
        if ele == 'a':
            # mark distance and save into 'cur'
            dist[r][c] = 0
            cur.append([c,r])
        c += 1
    print('')
    r += 1
steps.append(cur)

# mark end point to be just past z?
m[20][77] = '{'
dist[20][0] = 0

# start loop
done = False
step = 0
while not done:
    step += 1
    dist, done, steps = mark_step(dist, m, step, steps)
    if step > 500:
        break

print(step)

r = 0
for row in dist:
    c = 0
    for ele in row:
        print('%3d%c' % (ele,m[r][c]), end='')
        c += 1
    print('')
    r += 1
