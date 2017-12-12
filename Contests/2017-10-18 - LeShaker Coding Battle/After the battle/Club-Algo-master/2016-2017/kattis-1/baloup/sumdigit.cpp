#include <iostream>
#include <cstdlib>


using namespace std;


int sumOfDigit(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}



int main() {

    while(1) {
        int input;
        cin >> input;
        if (input == 0)
            return 0;
        for (int p=11; p<=100000; p++) {
            if (sumOfDigit(input * p) == sumOfDigit(input)) {
                cout << p << endl;
                break;
            }
        }
    }


}
