for _ in range(1):
    
    li =[1,2,3,4,5]
    re = []
    for i in range(len(li)-1,-1,-1):
        a = li[i]
        b = li[i:len(li)]
        print(i,a,b)
        if a>=max(b):
            re.append(a)
    print(*re)
