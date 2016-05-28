import java.lang.Iterable;
import java.util.Vector;
public class Graph{
	private final int V;
	private Vector[] adj;

	public Graph(int v){
		this.V = V;
		adj = (Vector[]) new Vector[V];
		for (int v=0;v<V ;v++ ) {
			adj[v] = new Vector();
		}
	}

	public void addEdge(int v, int w){
		adj[v].add(w)
		adj[w].add(v)
	}

	public Interable<Integer> adj(int v){
		return adj[v];
	}
}