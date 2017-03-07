import java.util.Stack;

public class dfspath{
	private boolean[] marked;
	private int[] edgeTo;
	private int s;

	public dfspath(Graph g, int s){
		marked = new boolean[g.V()];
		edgeTo = new int[g.V()];
		this.s = s;
		dfs(g, s);
	}

	public void dfs(Graph g, int v){
		marked[v]=true;
		for (int node : g.adj(v)) {
			if(marked[node] == false){
				edgeTo[node]=v;
				dfs(g, node);
			}
		}
	}
	
	public boolean hasPathTo(int v){
		return marked[v];
	}

	public Iterable<Integer> pathTo(int v){
		if(hasPathTo(v)==false) return null;
		Stack<Integer> path = new Stack<Integer>();
		for (int i=v;i!=this.s ;i=edgeTo[i] ) {
			path.push(i);
		}
		path.push(this.s);
		return path;
	}
	
	public void PrintPath(int v){
		Stack<Integer> tmp = (Stack<Integer>)this.pathTo(v);
		System.out.print(tmp.pop());
		while(tmp.empty()!=true){
			System.out.print("->"+tmp.pop());
		}
	}
}