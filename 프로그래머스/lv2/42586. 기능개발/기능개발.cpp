#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {

    vector <int> work;
    vector<int> answer;
   

 // 프로그래스 값을 남은 일수로 바꿈.
    for (int i = 0; i < progresses.size(); i++)
    {
         progresses[i] = 100 - progresses[i];
    }
  //배포가 완성되기까지의 남은 일 수를 계산해서 work 벡터에 넣기
    for (int i = 0; i < progresses.size(); i++)
    {
        if (progresses[i] % speeds[i] == 0) // 나머지가 없다면 딱 맞는 날에 배포
            work.push_back(progresses[i] / speeds[i]);
        else // 나머지가 있다면 하루 뒤에 배포
            work.push_back((progresses[i] / speeds[i]) + 1);
    }
    int start =0;
    int tmp =0;
    while (start < work.size()){
        int next = start +1;
        while (next <work.size() && work[start] >= work[next]){
            next++;
        }
        answer.push_back(next-start);
        tmp += (next-start);
        start = next;
    }
    return answer;
    
    // 만약 작업물(progresses)이 남아 있다면
    if(tmp<work.size())
        answer.push_back(1);
   
}
