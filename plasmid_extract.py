with open(input(), mode='r') as table:
    for i in table.readlines():
        a = i.split('\t')
        if a[4] != 'chromosome':
            print(a)
