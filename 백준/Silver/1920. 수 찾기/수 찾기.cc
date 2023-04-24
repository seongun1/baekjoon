#include <iostream>

using namespace std;

int* arr1,*arr2;
int n1,n2;
void quicksort(int a, int b, int *arr) // a가 left , b가 right
{
	if (a >= b) return;
	int pivot = arr[(a + b) / 2];
	int left = a;
	int right = b;

	while (left <= right)
	{
		while (arr[left] < pivot) left++;
		while (arr[right] > pivot) right--;
		if (left <= right)
		{
			swap(arr[left], arr[right]);
				left++; 
				right--;
		}
	}
	quicksort(a, right,arr);
	quicksort(left, b,arr);
}

void binarysearch(int number)
{
		int first = 0, last = n1 - 1;
		while (first <= last)
		{
			int middle = (first + last) / 2;
			if (arr1[middle] == number)
			{
				cout << 1 << "\n";
				break;
			}
			else if (arr1[middle] < number) {
				first = middle + 1;
				continue;
			}
			else if (arr1[middle] > number) {
				last = middle - 1;
				continue;
			}
		}
		if (first > last) {
			cout << 0 << "\n";
		}
	
}
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> n1;
	arr1 = new int[n1];
	int k1;
	for (int i = 0; i < n1; i++)
	{
		cin >> k1;
		arr1[i] = k1;
	}
	
	// 받은 배열을 정렬하기
	quicksort(0, n1- 1, arr1); // 벡터를 사용할 수 있지만, quick정렬의 개념을 배우고자 직접 코드로 구현.
	

	//비교할 배열 생성
	cin >> n2;
	arr2 = new int[n2];
	int k2;
	for (int i = 0; i < n2; i++)
	{
		cin >> k2;
		arr2[i] = k2;
		binarysearch(k2);
	}

	// 이진 탐색 코드
	
	delete[] arr1;
	delete[] arr2;
}