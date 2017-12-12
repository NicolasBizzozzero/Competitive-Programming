#include <iostream>
#include <cstdlib>


using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i<n; i++) {
        int v;
        cin >> v;
        if (abs(v)%2==0) {
            cout << v << " is even" << endl;
        }
        else {
            cout << v << " is odd" << endl;
        }
    }
}
