n = int(input())

for _ in range(n):
    
    st = input()
    
    frq = [0]*26
    for i in range(len(st)):
        frq[ord(st[i])-97]+=1
        
    flag = 0
    print(frq)
    for i in range(0,26):
        if(frq[i]>=1):
            print('{}={}'.format(chr(i+97),frq[i]),end=' ')
            flag = 1 
    if(flag==0):
        print('-1')