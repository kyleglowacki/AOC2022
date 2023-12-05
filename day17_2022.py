import aocd


next_rock = 0

raw = aocd.get_data(day=17, year=2022)

data = raw.splitlines()

print(len(data))

# max puzzle height time
board = []
maxB = 5*2023
curMax = maxB-1

# init board
row = [0]*7
for i in range(0,maxB):
    board.append(row)

# index into data
di = 0

## ???
