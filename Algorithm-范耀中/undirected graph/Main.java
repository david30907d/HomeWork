import java.util.*;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner cin=new Scanner(System.in);
		Graph g = new Graph(8);
		g.addEdge(0, 1);
		g.addEdge(0, 2);
		g.addEdge(0, 5);
		g.addEdge(4, 5);
		g.addEdge(4, 3);
		g.addEdge(5, 3);
		g.addEdge(6, 7);
		dfspath d=new dfspath(g, 0);
		d.PrintPath(3);
		System.out.println();
		bfspath b=new bfspath(g, 0);
		b.PrintPath(3);
		System.out.println();
		connected_component c=new connected_component(g);
		System.out.println(c.connected(4, 5));
		System.out.println(c.connected(6, 0));
	}

}
