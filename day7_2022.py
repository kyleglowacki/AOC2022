
def div(dirs):
    dd = dirs[1:].split('/')
    dd = [ele for ele in dd if ele != '']
    return dd

def build(dirs):
    if len(dirs) > 0:
        if dirs[0] != '/':
            return '/' + '/'.join(c for c in dirs) + '/'
        else:
            return '/'.join(c for c in dirs)
    else:
        return '/'

def update(cwd, cmd):
    dd = div(cwd)
    if cmd == '..':
        dd = dd[:-1]
    else:
        #print(f'Appending {cmd} to {dd}')
        dd.append(cmd)
    return build(dd)

def get_val(k, d):
    for key, value in d.items():
        if key == k:
            return value
    return 0

def dir_cnt(base):
    return base.count('/')

def compute_size(base, tree):
    bs = 0
    os = 0
    for k,v in tree.items():
        if k == base:
            #print(f'Base size for dir {k} is {v}')
            bs = v
        elif (base in k) and (dir_cnt(base)+1 == dir_cnt(k)):
            ds = compute_size(k, tree)
            os += ds
            #print(f'Adding in size for dir {k} at {ds}')
    #print(f'{base} Total is {bs} + {os} = {bs+os}')
    return bs + os

import aocd

raw = aocd.get_data(day=7, year=2022)
# '127\n147\n148\n147\n146\n153\n ... '

data = raw.splitlines()
# ['127', '147', '148', ... ]

#data = ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']



cwd = '/'
ls_mode = False
dfk = {}
ls_file = 0

for d in data:
    ops = d.split()
    f,l = ops[0], ops[1:]
    if f == '$':
        if ops[1] == "cd":
            #print(f'Before Update "{cwd}"')
            cwd = update(cwd, ops[2])
            if ops[2] != "..":
                dfk.update({cwd: 0})
            #print(f'Update "{cwd}" to zero')
            ls_mode = False
        elif ops[1] == "ls":
            #print("LS")
            ls_mode = True
            ls_file = 0
        else:
            print("Other command???")
    else:
        if ls_mode:
            sz = ops[0]
            name = ops[1]
            if ls_file == 0:
                ds = get_val(cwd, dfk)
                if ds > 0:
                    print(f"LS SAME DIRECTORY TWICE {cwd}")
            try:
                size = int(sz)
                size += get_val(cwd, dfk)
                dfk.update({cwd: size})
                #print(f"Size of {cwd} now {dfk[cwd]}")
                ls_file += 1
            except ValueError:
                pass
        else:
            print("NOT IN LS MODE")

totals = {}
# UGH ... now add up subdirectories
for k,v in dfk.items():
    sz = compute_size(k, dfk)
    #print(f'TOTAL for {k} is size = {sz}')
    totals[k] = sz

# TODO
small_sum = 0
for k,v in totals.items():
    if v <= 100000:
        #print(f"Key = {k} and Val = {v}")
        small_sum += v

TOTS = compute_size('/', dfk)
left = TOTS - 40000000
print(f'{TOTS} but left {left}')

# TODO
all = []
for k,v in totals.items():
    if v > left:
        print(f"BIGS Key = {k} and Val = {v}")
        all.append(v)

print(small_sum)
print(sorted(all))
