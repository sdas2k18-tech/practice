#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool armstrogNo(int n){
    int sum = 0;
    int N = n;
    int dup = n;

    if (n <0){
        return false;
    }

    while(N!=0){

        int digit= N%10;
        sum= sum + digit*digit*digit;
        N=N/10;
    }
    if( dup == sum){
        return true;
    }
    else{
        return false;
    }
    
}

int main(){
    int n;
    cout << "enter a number";
    cin >> n;
    int a = armstrogNo(n);
    cout<< "armdtrong :"<< a << endl;
    return 0;
}

