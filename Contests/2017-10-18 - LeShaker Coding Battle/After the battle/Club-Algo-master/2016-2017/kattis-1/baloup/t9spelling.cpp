#include <iostream>
#include <cstdlib>
#include <string>
#include <map>

using namespace std;

int main() {
    map<char, string> mapping;
    mapping['1'] = "1";
    mapping['a'] = "2"; mapping['b'] = "22"; mapping['c'] = "222"; mapping['2'] = "2222";
    mapping['d'] = "3"; mapping['e'] = "33"; mapping['f'] = "333"; mapping['3'] = "3333";
    mapping['g'] = "4"; mapping['h'] = "44"; mapping['i'] = "444"; mapping['4'] = "4444";
    mapping['j'] = "5"; mapping['k'] = "55"; mapping['l'] = "555"; mapping['5'] = "5555";
    mapping['m'] = "6"; mapping['n'] = "66"; mapping['o'] = "666"; mapping['6'] = "6666";
    mapping['p'] = "7"; mapping['q'] = "77"; mapping['r'] = "777"; mapping['s'] = "7777"; mapping['7'] = "77777";
    mapping['t'] = "8"; mapping['u'] = "88"; mapping['v'] = "888"; mapping['8'] = "8888";
    mapping['w'] = "9"; mapping['x'] = "99"; mapping['y'] = "999"; mapping['z'] = "9999"; mapping['9'] = "99999";
    mapping[' '] = "0";

    int n;
    cin >> n;

    for (int i = 0; i<n; i++) {
        string in;
        do {
            getline(cin, in);
        } while (in.size() == 0);
        cout << "Case #" << (i+1) << ": ";

        char lastKey = ' ';
        for (int i = 0; i < in.length(); i++) {
            string keys = mapping[in[i]];
            if (keys[0] == lastKey)
                cout << " ";
            lastKey = keys[0];
            cout << keys;
        }
        cout << endl;
    }
}
