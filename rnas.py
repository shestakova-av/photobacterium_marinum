RNAS = {"rRNA": [0, set()],
             "tRNA": [0, set()],
             "RNA": [0, set()]}
with open(input(), mode='r') as table:
    columns = table.readline().split('\t')
    name = columns.index("class")
    for i in table.readlines():
        a = i.split('\t')
        for j in RNAS.keys():
            RNAS[j][1].add(a[0] * int(j in a[name]))
            RNAS[j][0] += int(j in a[name])
for i in RNAS:
    print(i, RNAS[i])
