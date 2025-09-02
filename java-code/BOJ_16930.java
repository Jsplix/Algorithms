import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	static class Pos {
		int r, c;

		Pos(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	static int N, M, K;
	static int sr, sc, tr, tc;
	static int[][] v;
	static char[][] graph;
	static Deque<Pos> q = new ArrayDeque<>();

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		graph = new char[N + 1][M + 1];
		v = new int[N + 1][M + 1];

		for (int i = 1; i <= N; i++) {
			Arrays.fill(v[i], -1);
			String line = br.readLine();
			for (int j = 1; j <= M; j++) {
				graph[i][j] = line.charAt(j-1);
			}
		}

		st = new StringTokenizer(br.readLine());
		sr = Integer.parseInt(st.nextToken());
		sc = Integer.parseInt(st.nextToken());
		tr = Integer.parseInt(st.nextToken());
		tc = Integer.parseInt(st.nextToken());
		
		
		int RESULT = BFS(tr, tc, sr, sc);
		sb.append(RESULT);

		System.out.println(sb);
	}

	static int BFS(int sr, int sc, int tr, int tc) {

		int[] dr = new int[] { 0, 1, 0, -1 };
		int[] dc = new int[] { -1, 0, 1, 0 };
		
		q.add(new Pos(sr, sc));
		v[sr][sc] = 0;

		while (!q.isEmpty()) {
			Pos cur = q.poll();

			for (int i = 0; i < 4; i++) {
				for (int w = 1; w <= K; w++) {
					int nr = cur.r + w * dr[i];
					int nc = cur.c + w * dc[i];
					
					if (nr <= 0 || nr > N || nc <= 0 || nc > M || graph[nr][nc] == '#') break; 
					
					if (nr == tr && nc == tc) {
						return v[cur.r][cur.c] + 1;
					}
					
					if (v[nr][nc] == -1 || v[nr][nc] != -1 && v[nr][nc] > v[cur.r][cur.c] + 1) {
						q.add(new Pos(nr, nc));
						v[nr][nc] = v[cur.r][cur.c] + 1;
					}
					
				}
				
			}
		}

		return -1;
	}
}
