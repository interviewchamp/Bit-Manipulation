#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    unsigned int num,pos1,pos2;
    
    cout<<"Enter an integer : \n";
    cin>>num;
    
    cout<<"Enter two positions to swap : \n";
    cin>>pos1>>pos2;
    
    unsigned int bit1 =  (num >> pos1) & 1;
    unsigned int bit2 =  (num >> pos2) & 1;

    unsigned int xor_result = (bit1 ^ bit2);

    xor_result = (xor_result << pos1) | (xor_result << pos2);
    
    unsigned int result = num ^ xor_result;
    
    cout<<"After swapping bits on position "<<pos1<<" and "<<pos2<<" the answer in integer is : "<<result<<endl;
    
    return 0;
}
