import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	
	static int n, m;
	static long[] arr, maxTree, minTree;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		n = Integer.parseInt(st.nextToken()); m = Integer.parseInt(st.nextToken());
		
		arr = new long[n]; maxTree = new long[4 * n]; minTree = new long[4 * n];
		
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.fill(maxTree, Long.MIN_VALUE);
		Arrays.fill(minTree, Long.MAX_VALUE);
		
		initMax(1, 0, n - 1);
		initMin(1, 0, n - 1);
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int l = Integer.parseInt(st.nextToken());
			int r = Integer.parseInt(st.nextToken());
			long mn = findMin(1, 0, n - 1, l - 1, r - 1);
			long mx = findMax(1, 0, n - 1, l - 1, r - 1);
			
			sb.append(mn).append(" ").append(mx).append("\n");
		}
		
		System.out.println(sb);
	}
	
	
	static long initMax(int node, int start, int end) {
		if (start == end) return maxTree[node] = arr[start];
		
		int mid = (start + end) / 2;
		
		long v1 = initMax(2 * node, start, mid);
		long v2 = initMax(2 * node + 1, mid + 1, end);
		return maxTree[node] = v1 > v2 ? v1: v2;
	}

	static long initMin(int node, int start, int end) {
		if (start == end) return minTree[node] = arr[start];
		
		int mid = (start + end) / 2;
		
		long v1 = initMin(2 * node, start, mid);
		long v2 = initMin(2 * node + 1, mid + 1, end);
		return minTree[node] = v1 < v2 ? v1: v2;
	}
	
	static long findMax(int node, int start, int end, int left, int right) {
		
		if (start > right || end < left) return Long.MIN_VALUE;
		
		if (left <= start && end <= right) {
			return maxTree[node];
		}
		
		int mid = (start + end) / 2;
		long m1 = findMax(2 * node, start, mid, left, right);
		long m2 = findMax(2 * node + 1, mid + 1, end, left, right);
		
		return m1 > m2 ? m1 : m2;
	
	}
	
	static long findMin(int node, int start, int end, int left, int right) {
		
		if (start > right || end < left) return Long.MAX_VALUE;
		
		if (left <= start && end <= right) {
			return minTree[node];
		}
		
		int mid = (start + end) / 2;
		long m1 = findMin(2 * node, start, mid, left, right);
		long m2 = findMin(2 * node + 1, mid + 1, end, left, right);
		
		return m1 < m2 ? m1 : m2;
	}
}

