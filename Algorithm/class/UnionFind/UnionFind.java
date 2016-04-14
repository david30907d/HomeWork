public class UnionFind{
	private int[] id;
	private int[] size;// used to record the num of tree.
	public UnionFind(int n){
		id=new int[n];
		size=new int[n];
		for (int i=0;i<n ;++i ) {
			id[i]=i;
			size[i]=1;
		}
	}
	public int find(int n){
		while(id[n]!=n){
			id[n]=id[id[n]];//Path Compression 這個點原本紀錄的事他的parent，現在讓他紀錄他的爺爺，也就是更靠近root，可以節省查詢時間
			n=id[n];
		}
		return id[n];
	}
	public void union(int p,int q){
		int pid=find(p);
		int qid=find(q);
		if(size[p]>size[q]){//兩顆樹合併都會讓被合併的那個樹所有node的height增加1，所以要挑小顆的樹併到高的
			id[qid]=pid;
			size[pid]++;
		}
		else{
			id[pid]=qid;
			size[qid]++;
		}
	}
	public boolean connected(int p,int q){
		return (find(p)==find(q));
	}
}	