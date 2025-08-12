import java.util.Scanner;

/**
 * [BOJ] 2042 구간 합 구하기 / 자료 구조, 세그먼트 트리
 */
public class Main {

    static int n, m, k;
    static long[] arr;
    static long[] tree;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        n = sc.nextInt(); m = sc.nextInt(); k = sc.nextInt();
        arr = new long[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLong();
        }

        tree = new long[4 * n];
        init(1, 0, n-1);

        for (int i = 0; i < m + k; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            long c = sc.nextLong();

            if (a == 1) {
                update(1, 0, n - 1, b - 1 , c - arr[b - 1]);
                arr[b-1] = c;
            } else {
                long sm = sum(1, 0, n - 1, b - 1, (int) c - 1);
                sb.append(sm).append("\n");
            }
        }

        System.out.println(sb);

    }

    static long init(int node, int start, int end) {

        if (start == end) {
            return tree[node] = arr[start];
        }

        int mid = (start + end) / 2;

        return tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end);
    }

    static long sum(int node, int start, int end, int left, int right) {

        if (left > end || right < start) return 0;

        if (left <= start && end <= right) return tree[node];

        int mid = (start + end) / 2;

        return sum(node*2, start, mid, left, right) + sum(node*2 + 1, mid + 1, end, left, right);
    }

    static void update(int node, int start, int end, int index, long diff) {
        if (index < start || end < index) return ;

        tree[node] += diff;

        int mid = (start + end) / 2;
        if (start != end) {
            update(node*2, start, mid, index, diff);
            update(node*2 + 1, mid + 1, end, index, diff);
        }
    }
}

