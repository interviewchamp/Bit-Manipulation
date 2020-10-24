#include <iostream>
#include <vector>
using namespace std;

int singleNumber(vector<int> &A) {
       int n = A.size();
       int result = 0;
       for (int i = 0; i < n; i++) {
           result ^= A[i];
       }
       return result;
    }
};

int main()
{
    vector<int> = v{1,2,1,3,2,4,4};
    cout<<singleNumber(v);
}
