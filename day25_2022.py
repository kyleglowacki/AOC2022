v = {'2':2, '1':1, '0':0, '-':-1, '=':-2}
def convert_to_dec(s, base=1):
    global v
    l = s[len(s)-1]
    r = s[:len(s)-1]
    if r == '':
        return v[l]*base
    else:
        return v[l]*base + convert_to_dec(r,base*5)

import aocd

raw = aocd.get_data(day=25, year=2022)
data = raw.splitlines()

digits = {c: i for i, c in enumerate('=-0123456789')}
real_digits = {c: i for i, c in enumerate('0123456789')}

def parse_number(number, digits, base):
    return sum(digits[digit] * (base ** i)
        for i, digit in enumerate(reversed(number.lower())))

def convert_to_snafu(d):
    value = ''
    while d:
        d, r = divmod(d, 5)
        match r:
            # Use remainder to update value
            case 0|1|2: value = str(r) + value
            # Make it divide an extra time (minus 2)
            case 3:
                d += 1
                value = '=' + value
            # Make it divide an extra time (minus 1)
            case 4:
                d += 1
                value = '-' + value
    return value
total = 0
for d in data:
    vd = convert_to_dec(d)
    print(f"{d} is {vd}")
    #b5 = parse_number(d, digits, 5)
    #print(b5)
    total += vd

print(f"Total - {total}")
print(f"SNAFU - {convert_to_snafu(total)}")


