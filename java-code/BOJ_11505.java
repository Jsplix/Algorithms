import java.util.Scanner;

public class BOJ_11505 {
	
	static int n, m, k;
	static long[] arr, tree;
	static int MOD = 1000000007;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		n = sc.nextInt(); m = sc.nextInt(); k = sc.nextInt();
		
		arr = new long[n]; tree = new long[4 * n];
		
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextLong();
		}
		
		init(1, 0, n - 1);
		
		for (int i = 0; i < m + k; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = sc.nextInt();
			
			if (a == 1) {
				update(1, 0, n - 1, b - 1, c);
				arr[b - 1] = c;
			} else {
				long result = prod(1, 0, n - 1, b - 1, c - 1);
				sb.append(result).append("\n");
			}
			
		}
		
		System.out.println(sb);
	}
	
	static long init(int node, int start, int end) {
		if (start == end) return tree[node] = arr[start];
		
		int mid = (start + end) / 2;
		return tree[node] = (init(2 * node, start, mid) * init(2 * node + 1, mid + 1, end)) % MOD;
	}
	
	static long prod(int node, int start, int end, int left, int right) {
		
		if (left > end || right < start) return 1;
		
		if (left <= start && end <= right) {
			return tree[node];
		}
		
		int mid = (start + end) / 2;
		return (prod(2 * node, start, mid, left, right) * prod(2 * node + 1, mid + 1, end, left, right)) % MOD;
		
	}
	
	static void update(int node, int start, int end, int index, int value) {
		
		if (index < start || end < index) return ;
		
		if (start == end) {
			tree[node] = value;
			return ;
		}

		int mid = (start + end) / 2;
		update(2 * node, start, mid, index, value);
		update(2 * node + 1, mid + 1, end, index, value);
		tree[node] = (tree[node << 1] * tree[(node << 1) + 1]) % MOD;
		
	}
}

