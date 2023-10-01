s = input()

s1 = s[:s.find('h')]
s2 = s[s.rfind('h')+1:]
print(s1+s2)
