import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] heights = new int[n];
		for (int i = 0; i < n; i++) {
			heights[i] = sc.nextInt();
		}

		Stack<int[]> s = new Stack<>();
		
		ArrayList<int[]> result = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			result.add(new int[] {0, 0}); // 건물 개수, 가장 가까운 건물 번호
		}
		
		
		s.add(new int[] {0, heights[0]}); // 건물 번호, 건물 높이
		for (int i = 1; i < n; i++) {
			
			int[] r = result.get(i);
			
			while (!s.isEmpty()) {
				int[] temp = s.peek();
				if (temp[1] <= heights[i]) {
					s.pop();
				} else {
					break;
				}
			}
			
			if (!s.isEmpty()) {
				int[] temp = s.peek();
				r[1] = temp[0];
			}
			r[0] += s.size();
			s.add(new int[] {i, heights[i]});
		}
		
		s.clear();
		
		s.add(new int[] {n-1, heights[n-1]});
		for (int i = n-2; i >= 0; i--) {
			
			int[] r = result.get(i);
			
			while (!s.isEmpty()) {
				int[] temp = s.peek();
				if (temp[1] <= heights[i]) {
					s.pop();
				} else {
					break;
				}
			}
			
			if (!s.isEmpty()) {
				int[] temp = s.peek();
				if (r[0] == 0) {
					r[1] = temp[0];
				} else {
					int pdist = Math.abs(i - r[1]);
					int ndist = Math.abs(i - temp[0]);
					if (ndist < pdist) {
						r[1] = temp[0];
					}
				}
			}

			r[0] += s.size();
			s.add(new int[] {i, heights[i]});
		}
		for (int i = 0; i < n; i++) {
			if (result.get(i)[0] == 0) {
				System.out.println(0);
			} else {
				System.out.println(result.get(i)[0] + " " + (int) (result.get(i)[1] + 1));
			}
		}
	}

}
