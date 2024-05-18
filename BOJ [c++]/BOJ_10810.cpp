#include <bits/stdc++.h>
using namespace std;
// [BOJ] 10810 공 넣기 / 구현, 시뮬레이션 
int main(void) {
	ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
	int n, m; cin >> n >> m;
	int baskets[101] = {0};

	for (int i = 0; i < m; i++) {
		int l, r, x; cin >> l >> r >> x;
		for (int j = l; j < r+1; j++) {
			baskets[j] = x;
		}
	}

	for (int k = 1; k <= n; k++) {
		cout << baskets[k] << " ";
	} cout << '\n';
}