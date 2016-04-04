import java.util.*;
import loader.TrashCanAb;
public class Main {
  public static void main(String args[]) { 
	  Scanner cin=new Scanner(System.in);
	  queue q=new queue();
	  int time = cin.nextInt();
	  for(int i=0;i<time;++i){
		  int num=cin.nextInt();
		  q.Insert(num); 
	  }
	  System.out.println(q.ToString());
	  q.Empty();
	  System.out.println(q.ToString());
	  cin.close();
  }
} 