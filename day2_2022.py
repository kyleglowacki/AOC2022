import aocd




raw = aocd.get_data(day=2, year=2022)
# 

data = raw.splitlines()


# convert to int
#data= [int(x) for x in data]

#print(data)

score = {"X": 1, "Y": 2, "Z" : 3}
win_pts = 6
lose_pts = 0
draw_pts = 3

beats = {"B" : "Z", "C" : "X", "A" : "Y"}
draw = {"A":"X", "B":"Y", "C":"Z"}

# TODO
# One way
#z = [1 for x in range(len(data)-1) if data[x+1] > data[x]]
#print(len(z))

# generates T/F array.. sum seems to count True
#z = [data[x+1] > data[x] for x in range(len(data)-1)]
#print(sum(z))

#data = ['A Y','B X', 'C Z']

def score_it(data, b, drawl, w, r, s):

    idx = 0
    pts = []
    for d in data:
        f,l = d.split()
        try:
            if b[f] == l:
                # WIN!
                pts.append(w + s[l])
                print(f"WIN {pts[idx]} with {f} and {l}\n")
            else:
                # DRAW!
                if drawl[f] == l:
                    pts.append(r + s[l])
                    print(f"DRAW {pts[idx]} with {f} and {l}\n")
                else:
                    # TRUMP!
                    pts.append(s[l])
                    print(f"TRUMP {pts[idx]} with {f} and {l}\n")
        except KeyError:
            print(f"Key Error at {idx} with {f} and {l}\n")

        idx += 1

    return pts
          
board = score_it(data, beats, draw, win_pts, draw_pts, score)

total = sum(board)
print(total)

def make_it(data, b, lose, w, r, s):
    # Last letter decides what happens x/lose, y/draw, z/win
    idx = 0
    pts = []
    for d in data:
        f,l = d.split()

        if l == 'Y':
            # force draw
            pts.append(r + s[draw[f]])
        if l == 'Z':
            # win
            pts.append(w + s[b[f]])
        if l == 'X':
            # lose
            pts.append(s[lose[f]])
        idx += 1

    return pts

b2 = {"B" : "Z", "C" : "X", "A" : "Y"}
l2 = {"A" : "Z", "B" : "X", "C" : "Y"}

board2 = make_it(data, beats, l2, win_pts, draw_pts, score)
t2 = sum(board2)
print(t2)
