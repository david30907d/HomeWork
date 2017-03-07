import java.lang.Iterable;
import java.util.ArrayList;
public class Graph{
	private final int V;
	private int E;
	private ArrayList<Integer>[] adj;

	public Graph(int V){
		this.V = V;
		adj = (ArrayList<Integer>[]) new ArrayList[V];
		for (int i=0;i<V ;i++ ) {
			adj[i] = new ArrayList<Integer>();
		}
	}
	
	public void addEdge(int v, int w){
		adj[v].add(w);
		adj[w].add(v);
		E++;
	}

	public Iterable<Integer> adj(int v){
		return adj[v];
	}

	public int V(){
		return V;
	}

	public int E(){
		return E;
	}

	public static int degree(Graph G, int v){
		int degree=0;
		for (int node : G.adj(v) ) {
			degree++;
		}
		return degree;
	}
}