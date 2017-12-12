#include <iostream>
#include <cstdlib>
#include <string>
#include <map>

using namespace std;

int main() {
    int nbTest;
    cin >> nbTest;
    for (int i=0; i<nbTest; i++) {
        int itemPrice;
        cin >> itemPrice;
        int nbBills;
        cin >> nbBills;
        map<int, int> bills;
        for (int j=0; j<nbBills; j++) {
            int bill;
            cin >> bill;
            auto search = bills.find(bill);
            if (search != bills.end()) {
                search->second++;
                cout << search->second << endl;
            }
            else {
                bills[bill] = 1;
            }

        }


        // TODO pas fini
    }
}
