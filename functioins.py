FUNCTIONS = {"ribosomal": 0,
             "hypothetical": 0,
             "transport": 0}

total = 0

with open(input(), mode='r') as table:
    columns = table.readline().split('\t')
    name = columns.index("name")
    print(name)
    feat = columns.index("# feature")
    cl = columns.index("class")
    for i in table.readlines():
        a = i.split('\t')
        if a[feat] == "CDS" and a[cl] == "with_protein":
            total += 1
            for j in FUNCTIONS.keys():
                FUNCTIONS[j] += int(j in a[name])
                
for i in FUNCTIONS:
    print(i, FUNCTIONS[i])
print("total", total)
