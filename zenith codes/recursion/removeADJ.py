def rem(st):
    if(len(st)==1):
        return st 
    if(st[0]==st[1]):
        return rem(st[1:])
    return st[0] + rem(st[1:])


st = input()
print(rem(st))