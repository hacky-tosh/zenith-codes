def fact(n):
    if n==1 or n==1:
        return n
    return n * fact(n-1)



def main():
    t = int(input())
    while(t>0):
        n = int(input())
        print(fact(n))
        t = t - 1 

if __name__ == "__main__":
    main()