import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static class Pair {
		int importance, time;

		Pair(int importance, int time) {
			this.importance = importance;
			this.time = time;
		}
	}

	static int N, K;
	static int[][] dp;
	static List<Pair> list = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		StringBuilder sb = new StringBuilder();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken()); K = Integer.parseInt(st.nextToken());
		
		dp = new int[K + 1][N + 1];
		for (int i = 0; i < K; i++)  {
			st = new StringTokenizer(br.readLine());
			list.add(new Pair(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		
		for (int i = 1; i <= K; i++) {
			Pair p = list.get(i - 1);
			for (int j = 0; j <= N; j++) {
				if (j < p.time) {
					dp[i][j] = dp[i - 1][j];
				} else {
					dp[i][j] = Math.max(dp[i - 1][j - p.time] + p.importance, dp[i - 1][j]);
				}
			}
		}
		
		sb.append(Arrays.stream(dp[K]).max().getAsInt());
		System.out.println(sb);
	}

}
