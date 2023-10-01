s = input()

a = s[s.find('h'):s.rfind('h')]
x = a[::-1]
y = s[0:s.find('h')+1]
z = s[s.rfind('h')+1:]
print(y+x+z)
