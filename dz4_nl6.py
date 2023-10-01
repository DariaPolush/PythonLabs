a = [int(i) for i in input().split()]
s = []
for i in a:
    if i in s:
        print('YES')
    else:
        print('NO')
    s.append(i)
