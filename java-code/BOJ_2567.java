import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M;
	static int[][] paper;
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		paper = new int[101][101];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			
			for (int r = y; r < y + 10; r++) {
				for (int c = x; c < x + 10; c++) {
					paper[r][c] = 1;
				}
			}
			
		}
		
		int area = 0;
		int[] dr = new int[] {0, -1, 0, 1};
		int[] dc = new int[] {-1, 0, 1, 0};
		for (int i = 1; i <= 100; i++) {
			for (int j = 1; j <= 100; j++) {
				if (paper[i][j] == 1) {
					for (int d = 0; d < 4; d++) {
						if (paper[i + dr[d]][j + dc[d]] == 0) area++;
					}
				}
			}
		}
		
		sb.append(area);
		
		System.out.println(sb);
	}
	
	
}
