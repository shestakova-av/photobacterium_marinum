with open(input(), mode='r') as seq:
    length = 0
    gc = 0
    at = 0
    for i in seq.readlines():
        if i[0] == '>':
            if gc != 0:
                print(str(length) * int(length != 0), end='\t')
                print(gc / (gc + at))
            length, gc, at = 0, 0, 0
            print(i.strip(), end='\t')
        else:
            for j in i:
                if j in ("A", "T"):
                    at += 1
                elif j in ("C", "G"):
                    gc += 1
            length += len(i.strip())
    print(length, end='\t')
    print(gc / (gc + at))
