#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


vector<char> fillVector() {
	vector<char> v;
	string chars = "abcdefghijklmnopqrstuvwxyz";
	for (int i=0; i<26; i++) {
		v.push_back(chars[i]);
	}
	return v;
}

void removeFromVector(vector<char>& v, char c) {
		vector<char>::iterator pos = find(v.begin(), v.end(), c);
		if (pos != v.end())
			v.erase(pos);
}



char easytolower(char in){
  if(in<='Z' && in>='A')
    return in-('Z'-'z');
  return in;
} 


int main() {
	int n;
	string str;
	
	cin >> n;
	getline(cin, str);
	
	for (int i=0; i<n; i++) {
		getline(cin, str);
		
		vector<char> chars = fillVector();
		
		for (int i=0; i<str.size(); i++) {
			removeFromVector(chars, easytolower(str[i]));
		}
		
		if (chars.size() == 0)
			cout << "pangram" << endl;
		else {
			cout << "missing ";
			for (int i=0; i<chars.size(); i++) {
				cout << chars[i];
			}
			cout << endl;
		}
		
	}
}
