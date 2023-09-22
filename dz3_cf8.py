s = []

with open('C:/Users/admin/Downloads/СФ8.txt') as file:
    for line in file:
        s.append(int(line))
mx = 0
mn = 0

for i in range(1, s[0]+1):
    if s[i] == max(s):
        mx = i
    if s[i] == min(s):
        mn = i

s[mx], s[mn] = s[mn], s[mx]

out = open('C:/Users/admin/Downloads/result.txt', 'w')

for i in range(1, s[0]+1):
    out.write(str(s[i]))
    out.write('\n')
    

out.close()
