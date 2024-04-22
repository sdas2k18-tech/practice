#include<bits/stdc++.h>
using namespace std;

// pass by value 
void doSomething(string &s){
    s[0]='t';
    cout<< s << endl;
}

int main(){
    string s= "Daz";
    doSomething(s);
    cout<< s << endl;
    return 0;
}