import aocd

FALSE = 1
TRUE = 2
KEEP_GOING = 3


# Must take a list f=first, l=last
def compare(f,l):
    print(f"Compare <{f}> and <{l}>")
    
    # BOTH INT
    if (type(f) is int) and (type(l) is int):
        print(f"Both Ints  {f}  {l}")
        if f == l:
            return KEEP_GOING
        if l < f:
            print("Last is less than first")
            return FALSE
        if f < l:
            print("First is less than last")
            return TRUE

    # ONE LIST, ONE INT
    if (type(f) is list) and (type(l) is int):
        print("First list, second int, convert to both lists")
        return compare(f,[l])

    if (type(f) is int) and (type(l) is list):
        print("First int, second list, convert to both lists")
        return compare([f],l)

    # BOTH ARE LIST
    
    num = max(len(f),len(l))
    for i in range(num):
        # Make sure index i exists
        f_exists = True
        l_exists = True
        try:
            f[i]
        except IndexError:
            f_exists = False
        try:
            l[i]
        except IndexError:
            l_exists = False

        if f_exists and l_exists:
            print(f"Call compare for index {i}")
            value = compare(f[i], l[i])
            if value != KEEP_GOING:
                print("Not keep going.. so return definitive value")
                return value
        elif l_exists:
            print("First ran out, but not last")
            return TRUE
        elif f_exists:
            print("Last ran out, but not first")
            return FALSE
        # else KEEP GOING
        print("KEEP GOING!")
    return KEEP_GOING
    
raw = aocd.get_data(day=13, year=2022)

raw1 = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
data = raw.splitlines()

print(data)
inp = []

for i in range(len(data)):
    print(f"{i} is <{data[i]}>")
    if i % 3 == 0:
        f = eval(data[i])
        l = eval(data[i+1])
        inp.append([f,l])

print(f"Input - {inp}")

cnt = 0
sum =0
for pair in inp:
    cnt += 1
    f = pair[0]
    l = pair[1]
    print(f"\n\n{cnt} -- {sum}")
    value = compare(f,l)
    if value == KEEP_GOING:
        print(f"Pair {cnt} is KEEP_GOING?!?!?")
        exit()
        
    if value == TRUE:
        sum += cnt
        print(f"Pair {cnt} is True - Adding to sum")
    else:
        print(f"Pair {cnt} is FALSE not adding to sum")
        
print(f"Sum = {sum}")
