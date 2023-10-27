files = dict()
right_list = {'read':'R', 'write': 'W', 'execute': 'X'}

for i in range(int(input())):
    file, *permissions = input().split()
    files[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if right_list[action] in files[file]:
        print('OK')
    else:
        print('Access denied')
