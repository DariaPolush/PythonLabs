s = []

with open('C:/Users/admin/Downloads/СФ5.txt') as file:
    for line in file:
        s.append(int(line))

schet = []

for i in range(1, s[0]+1):
    if s[i] % 2 == 0:
        schet.append(s[i])

out = open('C:/Users/admin/Downloads/result.txt', 'w')

for i in range(len(schet)):
    out.write(str(schet[i]))
    out.write('\n')
    
out.close()
