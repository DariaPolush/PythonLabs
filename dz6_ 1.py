a, b = map(float, input().split())
def careless_div(a, b):
    if b == 0:
        if a == 0:
            return -17.5
        elif a > 0:
            return 'inf'
        else:
            return '-inf'
    else:
        return a/b
if careless_div(a, b) == 'inf' or careless_div(a, b) == '-inf' or int(careless_div(a, b)) != careless_div(a, b):
    print(careless_div(a, b))
else:
    print(int(careless_div(a, b)))
