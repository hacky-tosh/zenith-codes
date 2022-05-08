st = input()
for i in range(len(st)):
    print(st[0:i+1])

for i in range(len(st)-1,-1,-1):
    print(st[i:len(st)])