n = int(input())
place = {}
for i in range(n):
    country, *cities = input().split()
    for city in cities:
        place[city] = country
        
m = int(input())
for f in range(m):
    print(place[input()])
