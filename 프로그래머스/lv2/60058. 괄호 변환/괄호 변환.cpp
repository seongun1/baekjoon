#include <string>
#include <vector>
#include <stack>
using namespace std;
char a = '(';
char b = ')';
bool is_right_string(string p) // 올바른 괄호 문자열이 맞는 지 판단
{
    stack<char> stk;
    for (int i = 0; i < p.length(); i++)
    {
        if (p[i] == a)
            stk.push(a);
        else
        {
            if (stk.size() == 0) // 만약 ')' 문자열이였다면, '('문자열이 있다면 같이 빼서 소거시키고 아니라면 올바른 괄호 문자열이 아님.
                return false;
            stk.pop();
        }
    }
    if (stk.size() > 0)
        return false;
    else
        return true;
}
string solution(string p) {
    //1.입력이 빈 문자열인 경우 빈 문자열을 반환
    if (p == "")
        return "";
    string answer = "";
    //2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    //단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    string u, v;
    int left = 0; int right = 0;
    for (int i = 0; i < p.length(); i++)
    {
        if (p[i] == a) left++;
        else if (p[i] == b) right++;

        if (left == right) {
            u = p.substr(0, i + 1);
            v = p.substr(i + 1);
            break;
        }
    }
    //3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if (is_right_string(u) == true) {
        v = solution(v);
        //3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        answer = u + v;
        return answer;
   }
   // 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else {
        //4 - 1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        string temp;
        temp = a;
       // 4 - 2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        temp += solution(v);
        //4 - 3. ')'를 다시 붙입니다.
        temp += b;
        //4 - 4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u.erase(0, 1);
        u.erase(u.length() - 1, 1);
        for (int i = 0; i < u.length(); i++)
            if (u[i] == a)
                temp += b;
            else
                temp += a;
        answer = temp;
    }
    return answer;
}