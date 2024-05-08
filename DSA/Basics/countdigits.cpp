                                
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


// Function to count the number
// of digits in an integer 'n'.
int countDigits(int n){
    int count=0;

    while(n>0){
        count= count +1 ;

        n= n/10;
    }
    return count;
    
}



int main() {
    int n;
    cout << "enter a number";
    cin >> n;
    int digits= countDigits(n);
    cout<< "no of digits :"<< digits << endl;
    return 0;
}

                                
                            