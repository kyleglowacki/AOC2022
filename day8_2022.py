import aocd

raw = aocd.get_data(day=8, year=2022)
data = raw.splitlines()

def v_from_left(x,y,w,h,d):
    if x == 0:
        # edge
        return True
    for idx in range(0,x):
        # every tree is less than
        if d[y][idx] >= d[y][x]:
            return False
    return True

def v_from_right(x,y,w,h,d):
    if x == w-1:
        # edge
        return True
    for idx in range(x+1,w):
        # every tree is less than
        if d[y][idx] >= d[y][x]:
            return False
    return True

def v_from_top(x,y,w,h,d):
    if y == 0:
        # edge
        return True
    for idx in range(0,y):
        # every tree is less than
        if d[idx][x] >= d[y][x]:
            return False
    return True

def v_from_bottom(x,y,w,h,d):
    if y == h-1:
        # edge
        return True
    for idx in range(y+1,h):
        # every tree is less than
        if d[idx][x] >= d[y][x]:
            return False
    return True

#w,h full range
#x,y tree in question
#d   dataset
def visible(x,y,w,h,d):
    if v_from_left(x,y,w,h,d):
        return 1
    if v_from_top(x,y,w,h,d):
        return 1
    if v_from_right(x,y,w,h,d):
        return 1
    if v_from_bottom(x,y,w,h,d):
        return 1
    return 0

def viewTop(x,y,w,h,d):
    if y == 0:
        # edge
        return 0
    cnt = 0
    for idx in range(y-1,-1,-1):
        # If tree is big/bigger
        if d[idx][x] >= d[y][x]:
            if x==14 and y==52:
                print(f'T.. bigger at {idx}/{x} value of {cnt}')
            return cnt+1
        else:
            cnt += 1
    if x==14 and y==52:
        print(f'T hit edge with {cnt}')  
    return cnt
def viewLeft(x,y,w,h,d):
    if x == 0:
        # edge
        return 0
    cnt = 0
    for idx in range(x-1,-1,-1):
        # If tree is big/bigger
        if d[y][idx] >= d[y][x]:
            if x==14 and y==52:
                print(f'L.. bigger at {y}/{idx} value of {cnt}')
            return cnt+1
        else:
            cnt += 1
    if x==14 and y==52: 
        print(f'L hit edge with {cnt}')  
    return cnt
def viewRight(x,y,w,h,d):
    if x == w-1:
        # edge
        return 0
    cnt = 0
    for idx in range(x+1,w):
        # If tree is big/bigger
        if d[y][idx] >= d[y][x]:
            if x==14 and y==52:
                print(f'R.. bigger at {y}/{idx} value of {cnt}')
            return cnt+1
        else:
            cnt += 1
    if x==14 and y==52:
        print(f'R hit edge with {cnt}')  
    return cnt
##########
def viewBottom(x,y,w,h,d):
    if y == h-1:
        # edge
        return 0
    cnt = 0
    for idx in range(y+1,h):
        # If tree is big/bigger
        if d[idx][x] >= d[y][x]:
            if x==14 and y==52:
                print(f'B.. bigger at {idx}/{x} value of {cnt}')
            
            return cnt+1
        else:
            cnt += 1
    if x==14 and y==52:
        print(f'B hit edge with {cnt}')  
    return cnt
#######
def scenic(x,y,w,h,d):
    t = viewTop(x,y,w,h,d)
    b = viewBottom(x,y,w,h,d)
    l = viewLeft(x,y,w,h,d)
    r = viewRight(x,y,w,h,d)
    return t*b*l*r

# convert to int
#data = ['30373','25512','65332','33549','35390']
idx = 0
for x in data:
    data[idx] = [int(y) for y in data[idx]]
    idx += 1

#print(data)

h = len(data)
w = len(data[0])

print(f'Grid is {h} and {w}')

# One way
#z = [1 for x in range(len(data)-1) if data[x+1] > data[x]]
#print(len(z))

# generates T/F array.. sum seems to count True
#z = [data[x+1] > data[x] for x in range(len(data)-1)]
#print(sum(z))

# Loop over all elements
vis = 0
for y in range(0,h):
    for x in range(0,w):
        vis += visible(x,y,w,h,data)

print(f'Total visible = {vis}')

scene = [0] * h
for y in range(0,h):
    scene[y] = [0]*w
for y in range(0,h):
    for x in range(0,w):
        scene[x][y] = scenic(x,y,w,h,data)

import numpy
a = numpy.array(scene)
xy = numpy.unravel_index(a.argmax(), a.shape)
print(f'Max Scenic at {xy} with value of {scene[xy[0]][xy[1]]}')
print(f'Max Scenic at {xy} with value of {scene[xy[1]][xy[0]]}')
