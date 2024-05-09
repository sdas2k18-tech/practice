#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool reverseDigits(int n){
    int dup = n;
    int rev= 0;
    int N = n;

    while(N!=0){

        int digit= N%10;
        rev= rev * 10 + digit;
        N=N/10;
    }
    if(dup == rev){
            return true;
        }
    else{
            return false;
        }
}

int main(){
    int n;
    cout << "enter a number to be check: ";
    cin >> n;
    bool revdigits= reverseDigits(n);
    cout<< revdigits << endl;
    return 0;
}

// 345
// %10 5 
// %