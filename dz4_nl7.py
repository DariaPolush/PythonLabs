n = int(input())
s = set()
for i in range(n):
    for j in input().split():
        s.add(j)
print(len(s))
