public class connected_component{
	private boolean[] marked;
	private int[] id;
	private int count=0;

	public connected_component(Graph g){
		marked = new boolean[g.V()];
		id = new int[g.V()];
		for (int v=0;v<g.V() ;v++ ) {
			if(marked[v]==false){
				dfs(g, v);
				count++;
			}
		}
	}

	public void dfs(Graph g, int v){
		marked[v]=true;
		id[v]=count;
		for(int node:g.adj(v)){
			if(marked[node]==false){
				dfs(g, node);
			}
		}
	}
	
	public int count(int v){
		return this.count;
	}

	public int id(int v){
		return id[v];
	}
	
	public boolean connected(int v, int w){
		return id[v]==id[w];
	}
}