#include <bits/stdc++.h>
using namespace std;
 
int increment(int number) {
    return (-(~number));
}

int main() {
    cout<<increment(1);
    return 0;
}
 