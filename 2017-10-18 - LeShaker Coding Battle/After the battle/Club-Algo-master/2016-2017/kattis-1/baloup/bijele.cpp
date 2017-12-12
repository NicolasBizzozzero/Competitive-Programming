#include <iostream>
#include <cstdlib>


using namespace std;

int main() {
    int values[] = {1, 1, 2, 2, 2, 8};

    for (int i = 0; i<6; i++) {
        int v;
        cin >> v;
        values[i] -= v;
    }

    cout << values[0] << " "
         << values[1] << " "
         << values[2] << " "
         << values[3] << " "
         << values[4] << " "
         << values[5];
}
