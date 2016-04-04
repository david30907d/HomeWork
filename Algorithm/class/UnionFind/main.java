import java.util.*;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner cin=new Scanner(System.in);
		UnionFind u = new UnionFind(10);
		u.union(1, 0);
		System.out.println("1 nd 3 is connected:"+u.connected(1, 3));
		u.union(5, 7);
		System.out.println("5 nd 7 is connected:"+u.connected(5, 7));
		u.union(8, 9);
		u.union(1, 5);
		System.out.println("5 nd 7 is connected:"+u.connected(5, 0));
	}

}
