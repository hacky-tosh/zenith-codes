# t = int(input())

# for _ in range(t):
#     st = input()
#     stli = list(st)
#     stli.sort()
#     stli.reverse()
#     print(''.join(stli))

t = int(input())

for _ in range(t):
    st = input()
    j = 0 
    temp = 0
    st1 = ''
    stl = list(st)
    

    for i in range(0,len(stl)):
        for j in range(0,len(stl)):
            if (stl[j]>stl[i]):
                temp = stl[i]
                stl[i] = stl[j]
                stl[j] = temp
    stl.reverse()
    print(''.join(stl))

