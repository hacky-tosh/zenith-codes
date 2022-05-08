def fib(n):
    if n==1 or n==0:
        return n
    return fib(n-1) + fib(n-2)




def main():
    t = int(input())
    while(t>0):
        n = int(input())
        print(fib(n))
        t = t - 1 

if __name__ == "__main__":
    main()