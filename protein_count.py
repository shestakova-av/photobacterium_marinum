with open(input(), mode='r') as table:
    plus, minus = 0, 0
    strand = table.readline().split('\t').index("strand")
    for i in table.readlines():
        a = i.split('\t')
        if a[0:2] == ['CDS', 'with_protein']:
            if a[strand] == '+':
                plus += 1
            else:
                minus += 1
    print(plus, minus)
