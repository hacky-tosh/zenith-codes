def resum(n):
  if  n==0 or n==1:
    return n
  return n + resum(n-1)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(resum(n))

if __name__=="__main__":
    main()