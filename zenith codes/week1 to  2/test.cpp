#include <bits/stdc++.h>
using namespace std;
int total_digits(int num){
   int count = 0;
   for(int i = 1; i <= num; i *= 10){
      count = count + (num - i + 1);
   }
   return count;
}
int main(){
  //  int num = 123;
  int t;
  while (t--)
  {
    int num;
    cin>>num;
   cout<<total_digits(num)<<endl;
       
  }
  
   return 0;
}