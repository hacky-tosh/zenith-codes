t = int(input())

for _ in range(t):
    st = input()
    vov = ['A','E','I','O','U']
    v = 0 
    c = 0
    for ele in st:
        if ele in vov:
            v = v + 1 
        else:
            c = c + 1
    print(v,c)



