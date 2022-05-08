def util(s):
   if len(s) & 1 != 0:
      return s
 
   left = util(s[0:int(len(s) / 2)])
   right = util(s[int(len(s) / 2):len(s)])
 
   return min(left + right, right + left)
 
def solve(s,t):
   return util(s) == util(t)

def main():
    t = int(input())
    while(t>0):
        st1 = input()
        st2 = input()
        if solve(st1, st2):
            print('YES')
        else:
            print('NO')
        t = t - 1 

if __name__ == "__main__":
    main()