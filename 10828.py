import sys
T = int(sys.stdin.readline())
li = []
for i in range(T):
    com = sys.stdin.readline()
    if com[:3] == 'pus':
        li.append(int(com[5:]))
    elif com[:3] == 'top':
        if len(li) == 0:
            print("-1")
        else:
            print(li[-1])
    elif com[:3] == 'siz':
        print(len(li))
    elif com[:3] == 'emp':
        if len(li) == 0:
            print("1")
        else:
            print("0")
    else:
        if len(li) == 0:
            print("-1")
        else:
            print(li[-1])
            li.pop(-1)
