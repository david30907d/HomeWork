import java.util.ArrayList;
import java.util.Stack;
public class bfspath{
	private boolean[] marked;
	private int[] edgeTo;
	private int[] distTo;
	private int s;

	public bfspath(Graph g, int s){
		marked = new boolean[g.V()];
		edgeTo = new int[g.V()];
		distTo = new int[g.V()];
		this.s = s;
		bfs(g, s);
	}

	public void bfs(Graph g, int v){
		ArrayList<Integer> q= new ArrayList();
		q.add(v);
		marked[v]=true;
		distTo[v]=0;
		while(!q.isEmpty()){
			int tmp = q.remove(0);
			for(int node : g.adj(tmp)){
				if(marked[node] == false){
					q.add(node);
					marked[node]=true;
					edgeTo[node]=tmp;
					distTo[node]=distTo[tmp]+1;
				}
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