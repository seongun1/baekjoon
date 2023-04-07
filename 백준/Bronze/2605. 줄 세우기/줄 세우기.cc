#include <iostream>
#include <vector>

using namespace std;

int main() {
	int number;
	cin >> number;
	int* a = new int[number];
	
	vector<int> v;
	for (int i = 0; i < number; i++)
	{
		cin >> a[i];
	}
	for (int i = 0; i < number; i++) {
		v.insert(v.begin()+a[i], i+1);
	}
	
	for (int i = v.size() - 1; i >= 0; i--) {
		cout << v[i] << " ";
	}
	delete [] a;
}