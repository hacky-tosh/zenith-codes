def sumn(n):
    if n==1 or n==1:
        return n
    return n + sumn(n-1)


def main():
    t = int(input())
    while(t>0):
        n = int(input())
        print(sumn(n))
        t = t - 1 

if __name__ == "__main__":
    main()