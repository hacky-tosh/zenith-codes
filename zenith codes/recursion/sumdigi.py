def sumn(n):
    if n==0 :
        return n
    return (n%10 + sumn(int(n/10)))


def main():
    t = int(input())
    while(t>0):
        n = int(input())
        print(sumn(n))
        t = t - 1 

if __name__ == "__main__":
    main()