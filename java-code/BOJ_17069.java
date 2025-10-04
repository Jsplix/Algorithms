import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int[][] home;
	static long[][][] dp;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());

		home = new int[N + 1][N + 1];
		dp = new long[3][N + 1][N + 1];
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				home[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 0 - 가로, 1 - 대각선, 2 - 세로
		dp[0][1][2] = 1; // :=> dp[d][r][c]: (r, c) 위치에서의 파이프 모양
		
		for (int r = 1; r <= N; r++) {
			for (int c = 3; c <= N; c++) {
				
				if (home[r][c] == 1) continue;
				
				if (home[r][c - 1] != 1) {
					dp[0][r][c] += dp[0][r][c - 1] + dp[1][r][c - 1];
				}
				if (home[r - 1][c] != 1) {
					dp[2][r][c] += dp[1][r - 1][c] + dp[2][r - 1][c];
				}
				if (home[r - 1][c - 1] != 1 && home[r - 1][c] != 1 && home[r][c - 1] != 1) {
					dp[1][r][c] += dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1];
				}
			}
		}

		
		sb.append(dp[0][N][N] + dp[1][N][N] + dp[2][N][N]);
		
		System.out.println(sb);
	}

}
