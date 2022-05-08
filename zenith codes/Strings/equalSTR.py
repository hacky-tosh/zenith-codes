t = int(input())

while(t>0):
    n = int(input())
    v = []
    for i in range(n):
        v.append(input())
    re = []
    for i in range(n):
        for j in range(n):
            str1 = v[i]
            str2 = v[j]
            varstr = v[j] + v[j]
            
            for k in range(len(varstr)):
                if varstr[k:len(str1)+k]==str1:
                    re.append(k)
                    break
    re = set(re)
    print(sorted(re)[1])
    t = t - 1
