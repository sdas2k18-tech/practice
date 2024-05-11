#include<bits/stdc++.h>
using namespace std;
int cnt = 0;

void print(){
   
   // Base Condition.
   if(cnt == 3)  return;
   cout<<"SDZ"<<" ";
 
   // Count Incremented
   cnt++;
   print();

}

int main(){
    print();
  return 0;
}
