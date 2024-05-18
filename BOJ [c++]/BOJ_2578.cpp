#include <bits/stdc++.h>
using namespace std;
// [BOJ] 2578 빙고 / 구현, 시뮬레이션
int check_row(int (*arr)[5]) {
	int ret = 0;
	for (int i = 0; i < 5; i++) {
		int chk = 0;
		for (int j = 0; j < 5; j++) {
			if (arr[j][i] == 0) chk++;
		}
		if (chk == 5) ret++;
	}
	return ret;
}

int check_col(int (*arr)[5]) {
	int ret = 0;
	for (int i = 0; i < 5; i++) {
		int chk = 0;
		for (int j = 0; j < 5; j++) {
			if (arr[i][j] == 0) chk++;
		}
		if (chk == 5) ret++;
	}
	return ret;
}

int check_diag(int (*arr)[5]) {
	int ret = 0;
	int l_chk = 0, r_chk = 0;
	for (int i = 0; i < 5; i++) {
		if (arr[i][i] == 0) l_chk++;
		if (arr[i][4-i] == 0) r_chk++;
	}
	if (l_chk == 5) ret++;
	if (r_chk == 5) ret++;
	return ret;
}

int main(void) {

	int inp_arr[5][5];
	int call_arr[5][5];

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cin >> inp_arr[i][j];
		}
	}
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cin >> call_arr[i][j];
		}
	}

	int call, cnt = 0;
	bool flag = false;
	for (int z = 0; z < 5; z++) {
		for (int h = 0; h < 5; h++) {
			call = call_arr[z][h];
			for (int x = 0; x < 5; x++) {
				for (int y = 0; y < 5; y++) {
					if (inp_arr[x][y] == call) {
						inp_arr[x][y] = 0;
						cnt++;
						break;
					}
				}
				if (check_col(inp_arr) + check_row(inp_arr) + check_diag(inp_arr) >= 3)  {
					cout << cnt;
					flag = true;
					break;
				}
			}
			if (flag) break;
		}
		if (flag) break;
	}
	return 0;
}