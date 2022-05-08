t = int(input())
for _ in range(t):
    q,p = map(int,input().split())
    if q>100:
        discount = ((p*q)*20)/100
        total_cost = (p*q) - discount
        print(total_cost)
    else:
        total_cost = ((q * p)*100/100) 
        print(total_cost)
