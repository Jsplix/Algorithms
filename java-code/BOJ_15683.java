import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N, M, result, min;
	static int[][] office, temp;
	static boolean[][] visited;
	static Queue<Camera> cctv = new LinkedList<>();
	static int[][] directions = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

	static class Camera {
		int r;
		int c;
		int num;

		Camera(int r, int c, int num) {
			this.r = r;
			this.c = c;
			this.num = num;
		}
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		office = new int[N][M];
		visited = new boolean[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				office[i][j] = Integer.parseInt(st.nextToken());
				if (office[i][j] >= 1 && office[i][j] <= 5) {
					cctv.add(new Camera(i, j, office[i][j]));
				}
				else if (office[i][j] == 6) {
					min--;
				}
			}
		}

		min = N * M - cctv.size();
		
		int all = pow(4, cctv.size());
		for (int i = 0; i < all; i++) {
			temp = new int[N][M];
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					temp[r][c] = office[r][c];
				}
			}
			
			int ti = i;
			for (Camera cam : cctv) {
				int nd = ti % 4;
				ti /= 4;
				
				if (office[cam.r][cam.c] == 1) {
					search(cam.r, cam.c, nd);
				} else if (office[cam.r][cam.c] == 2) {
					search(cam.r, cam.c, nd);
					search(cam.r, cam.c, nd + 2);
				} else if (office[cam.r][cam.c] == 3) {
					search(cam.r, cam.c, nd);
					search(cam.r, cam.c, nd + 1);
				} else if (office[cam.r][cam.c] == 4) {
					search(cam.r, cam.c, nd);
					search(cam.r, cam.c, nd + 1);
					search(cam.r, cam.c, nd + 2);
				} else if (office[cam.r][cam.c] == 5) {
					search(cam.r, cam.c, nd);
					search(cam.r, cam.c, nd + 1);
					search(cam.r, cam.c, nd + 2);
					search(cam.r, cam.c, nd + 3);
				}

			}

			int count = 0;
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					if (temp[r][c] == 0)
						count++;
				}
			}
			min = Math.min(min, count);
		}
		
		sb.append(min);
		System.out.println(sb);
	}

	static int pow(int base, int exp) {
		int ret = 1;
		while (exp != 0) {
			ret *= base;
			exp--;
		}
		return ret;
	}

	static void search(int pr, int pc, int d) {
		d %= 4;
		while (true) {
			pr += directions[d][0];
			pc += directions[d][1];

			if (pr < 0 || pr >= N || pc < 0 || pc >= M) {
				return ;
			}
			if (temp[pr][pc] == 6) {
				return ;
			}
			else if (temp[pr][pc] != 0) {
				continue;
			}
			temp[pr][pc] = 7;
		}
	}

}
