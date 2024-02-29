#include <iostream>
#include <algorithm>
// [BOJ] 15688 수 정렬하기 5 / 정렬
using namespace std;

bool comp(int a, int b) {
    return a < b;
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n; cin >> n;
    int* arr = new int[n];

    for (int i = 0; i < n; i++) cin >> arr[i];
    sort(arr, arr + n, comp);
    for (int i = 0; i < n; i++) cout << arr[i] << '\n';

    delete[] arr;

    return 0;
}