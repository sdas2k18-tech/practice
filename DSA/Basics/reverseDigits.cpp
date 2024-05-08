#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int reverseDigits(int n){
    int rev= 0;
    int N = n;

    while(N!=0){

        int digit= N%10;
        rev= rev * 10 + digit;
        N=N/10;
    }
    return rev;
}

int main(){
    int n;
    cout << "enter a number";
    cin >> n;
    int revdigits= reverseDigits(n);
    cout<< "reverse number :"<< revdigits << endl;
    return 0;
}

// 345
// %10 5 
// %