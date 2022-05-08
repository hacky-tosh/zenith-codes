def toh(n,s,d,h):
    if n==1:
        print("Move disk from ",s," to ",d)
        return 
    toh(n-1, s, d, h)
    print("Move disk from ",s," to ",d)
    toh(n-1, h, d, s)

def main():
    n = int(input())
    toh(n,1,3,2)

if __name__=='__main__':
    main()