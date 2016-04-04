import java.util.*;
public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Threesum t=new Threesum();
		Scanner cin=new Scanner(System.in);
		int[] arr=new int[8];
		for(int i=0;i<8;++i){
			arr[i]=cin.nextInt();
		}
		System.out.println(t.count(arr));
		
	}

}
