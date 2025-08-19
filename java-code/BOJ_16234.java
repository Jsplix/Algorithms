import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static class Pos {
		int r;
		int c;
		int p;

		Pos(int r, int c, int p) {
			this.r = r;
			this.c = c;
			this.p = p;
		}
	}

	static int N, L, R;
	static int[][] A, visited;
	static boolean flag = false;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		A = new int[N][N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int count = 0; count <= 2000; count++) {
			
			if (N == 1) {
				sb.append(0);
				break;
			}
			
			flag = false;
			visited = new int[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (visited[i][j] == 0) {
						BFS(i, j);
					}
				}
			}
			
			if (!flag) {
				sb.append(count);
				break;
			}
			
		}
		
		System.out.println(sb);
		

	}

	static void BFS(int pr, int pc) {
		
		Queue<Pos> q = new LinkedList<>();
		List<Pos> list = new LinkedList<>();
		q.add(new Pos(pr, pc, A[pr][pc]));
		
		int[] dr = {0, -1, 0, 1};
		int[] dc = {-1, 0, 1, 0};
		
		int area = 1;
		int total = A[pr][pc];
		visited[pr][pc] = 1;
		
		while (!q.isEmpty()) {
			Pos pos = q.poll();
			list.add(pos);
			int r = pos.r;
			int c = pos.c;
			int p = pos.p;
					
			for (int i = 0; i < 4; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];
				
				if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
				if (visited[nr][nc] == 1) continue;
				
				
				int diff = Math.abs(A[nr][nc] - p);
				
				if (diff >= L && diff <= R) {
					flag = true;
					q.add(new Pos(nr, nc, A[nr][nc]));
					total += A[nr][nc];
					visited[nr][nc] = 1;
					area++;
				}
				
			}
		}
		
		int after = total / area;
		for (int i = 0; i < list.size(); i++) {
			Pos temp = list.get(i);
			A[temp.r][temp.c] = after;
		}
		
		if (area == N * N) flag = true;
		
	}

}
