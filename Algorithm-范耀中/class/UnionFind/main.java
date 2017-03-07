import java.util.*;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner cin=new Scanner(System.in);
		UnionFind u = new UnionFind(10);
		u.union(1, 2);
		u.union(3, 4);
		u.union(4, 9);
		u.union(8, 4);

		u.union(5, 6);
		u.union(5, 0);
		u.union(7, 2);

		u.union(6, 1);
		u.union(7, 3);
		System.out.println(u.connected(9,1));
	}

}
