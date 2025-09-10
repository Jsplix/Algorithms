import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	static class Edge {
		int node, weight;
		boolean flag;
		
		Edge(int node, int weight) {
			this.node = node;
			this.weight = weight;
		}

		Edge(int node, int weight, boolean flag) {
			this.node = node;
			this.weight = weight;
			this.flag = flag;
		}
	}
	
	static int N, M;
	static int[] foxDist;
	static int[][] wolfDist;
	static ArrayList<Edge>[] graph;
	static PriorityQueue<Edge> pq;
	

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());

		graph = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}
		
		foxDist = new int[N + 1];
		wolfDist = new int[2][N + 1];
		Arrays.fill(foxDist, Integer.MAX_VALUE);
		Arrays.fill(wolfDist[0], Integer.MAX_VALUE);
		Arrays.fill(wolfDist[1], Integer.MAX_VALUE);
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			
			graph[a].add(new Edge(b, 2 * d));
			graph[b].add(new Edge(a, 2 * d));
		}
		
		wolfDijkstra();
		foxDijkstra();
		
		int result = 0;
		for (int i = 2; i <= N; i++) {
			if (foxDist[i] < Math.min(wolfDist[0][i], wolfDist[1][i])) result++;
		}
		
		sb.append(result);
		System.out.println(sb);

	}
	
	static void foxDijkstra() {
		
		pq = new PriorityQueue<>((e, v) -> {
			return Integer.compare(e.weight, v.weight);
		});
		
		pq.add(new Edge(1, 0));
		foxDist[1] = 0;
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			
			if (now.weight > foxDist[now.node]) continue;
			
			for (Edge next : graph[now.node]) {
				int nextDist = now.weight + next.weight;
				
				if (nextDist < foxDist[next.node]) {
					foxDist[next.node] = nextDist;
					pq.add(new Edge(next.node, nextDist));
				}
			}
		}
		
	}
	
	static void wolfDijkstra() {
		
		pq = new PriorityQueue<>((e, v) -> {
			return Integer.compare(e.weight, v.weight);
		});
		
		pq.add(new Edge(1, 0, false));
		wolfDist[0][1] = 0;
		
		while (!pq.isEmpty()) {
			Edge now = pq.poll();
			
			if (now.weight > wolfDist[now.flag ? 1 : 0][now.node]) continue;
			
			for (Edge next : graph[now.node]) {
				int nextDist = now.weight;
				boolean nextFlag = false;
				if (now.flag) {
					nextDist += (next.weight * 2);
					nextFlag = false;
				} else {
					nextDist += next.weight / 2;
					nextFlag = true;
				}
				
				if (nextDist < wolfDist[nextFlag ? 1 : 0][next.node]) {
					wolfDist[nextFlag ? 1 : 0][next.node] = nextDist;
					pq.add(new Edge(next.node, nextDist, nextFlag));
				}
			}
		}
	}
}
