import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static class Link{
		int from;
		int to;
		int weight;
		
		Link(int from, int to, int weight) {
			this.from = from;
			this.to = to;
			this.weight = weight;
		}
	}
	
	static int N, M, a, b, c, result;
	static int[] parents;
	static List<Link> graph;
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		
		parents = new int[N + 1];
		for (int i = 1; i <= N; i++) parents[i] = i;
		
		graph = new ArrayList();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken()); b = Integer.parseInt(st.nextToken()); c = Integer.parseInt(st.nextToken());
			graph.add(new Link(a, b, c));
		}
		graph.sort((e, v) -> { return e.weight - v.weight; });
		
		for (Link lnk : graph) {
			int pFrom = find(lnk.from);
			int pTo = find(lnk.to);
			
			if (pFrom != pTo) {
				union(pFrom, pTo);
				result += lnk.weight;
			}
			
		}
		sb.append(result);

		System.out.println(sb);

	}

	static void union(int x, int y) {
		int px = find(x);
		int py = find(y);
		
		if (px < py) {
			parents[py] = px;
		} else {
			parents[px] = py;
		}
	}
	
	static int find(int x) {
		if (parents[x] != x) return parents[x] = find(parents[x]);
		return parents[x];
	}
}
