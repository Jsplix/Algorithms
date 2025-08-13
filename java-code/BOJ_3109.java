import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int r, c, result = 0;
    static char[][] map;
    static int[] dr, dc;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        dr = new int[]{-1, 0, 1};
        dc = new int[]{1, 1, 1};

        map = new char[r][c];
        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        for (int i = 0; i < r; i++) {
            dfs(0, i, 0);
        }

        sb.append(result).append("\n");
        System.out.println(sb);
    }

    static boolean dfs(int depth, int pr, int pc) {

        if (depth == c - 1) {
            map[pr][pc] = 'x';
            result++;
            return true;
        }

        for (int i = 0; i < 3; i++) {
            int nr = pr + dr[i];
            int nc = pc + dc[i];
            if (nr < 0 || nr >= r || nc < 0 || nc >= c) continue;
            if (map[nr][nc] == '.') {
                boolean ret = dfs(depth + 1, nr, nc);
                if (!ret) map[nr][nc] = '-';
                if (map[nr][nc] == 'x') {
                    map[pr][pc] = 'x';
                    return true;
                }
            }
        }

        return false;
    }

}
