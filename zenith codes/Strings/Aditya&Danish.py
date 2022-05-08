t = int(input())

while(t>0):
    n = int(input())
    st = input()
    arr = list(st)
    a = 0
    d = 0
    for ele in arr:
        if ele=='A':
            a = a + 1 
        if ele=='D':
            d = d + 1 

    if a>d:
        print('Aditya')
    elif d>a:
        print('Danish')
    else:
        print('AdiDan')

    t = t - 1