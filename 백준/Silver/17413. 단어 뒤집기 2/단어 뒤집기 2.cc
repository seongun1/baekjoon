#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main() {
	string total; // 전체 문자열을 담을 변수
	
	getline(cin, total);

	stack <char> st;
	bool tag = false;
	for (char ch : total) {
		if (ch == '<') {
			// 중간에 < 문자열을 만난다면 그 전의 문자열을 다 비워내야 함.
			while (!st.empty()) {
				cout << st.top();
				st.pop();
			}
			tag = true;
			cout << ch;
		}
		else if (ch == '>') {
			tag = false;
			cout << ch;
		}
		else if (tag) // <> 내부의 글자
		{
			cout << ch;
		}
		else // <> 외부의 글자
		{
			if (ch == ' ')
			{
				while (!st.empty())
				{
					cout << st.top();
					st.pop();
				}
				cout << ch;
			}
			else
				st.push(ch);
		}
	}
	while (!st.empty())
	{
		cout << st.top();
		st.pop();
	}

}