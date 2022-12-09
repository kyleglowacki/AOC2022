import aocd




raw = aocd.get_data(day=4, year=2022)
# '127\n147\n148\n147\n146\n153\n ... '

data = raw.splitlines()
# ['127', '147', '148', ... ]

#print(data)

cnt = 0
cnt2 = 0
for d in data:
    f,l = d.split(',')
    ff,fl = f.split('-')
    lf,ll = l.split('-')
    ff = int(ff)
    fl = int(fl)
    lf = int(lf)
    ll = int(ll)

    if ((ff<=lf and fl>=ll) or (lf<=ff and ll>=fl)):
        cnt = cnt + 1
    if (((fl>=lf) and (ff <= ll)) or ((ll>=ff) and (lf <= fl))):
        cnt2 = cnt2 + 1
print(cnt)
print(cnt2)
    
# convert to int
#data= [int(x) for x in data]


# One way
#z = [1 for x in range(len(data)-1) if data[x+1] > data[x]]
#print(len(z))

# generates T/F array.. sum seems to count True
#z = [data[x+1] > data[x] for x in range(len(data)-1)]
#print(sum(z))

