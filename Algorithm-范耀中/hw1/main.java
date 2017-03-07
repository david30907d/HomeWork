import java.util.*;
import java.util.Random;
public class Main {
  public static void main(String args[]) { 
	  Scanner cin=new Scanner(System.in);
	  double[] input=new double[10];
      for(int i=0;i<10;++i){
	      input[i]=cin.nextDouble();
      }
	  ArrayData a=new ArrayData(input);
	  double max=a.max();
	  System.out.println(max);
	  double avg=a.avg();
	  System.out.println(avg);
	  for(int i=0;i<10;++i){
		  input[i]=cin.nextDouble();
	  }
	  double inn=a.inner_product(input);
	  System.out.println(inn);
	  a.reverse();
	  System.out.println(a.toString());
	  a.shuffle();
	  System.out.println(a.toString());
	  cin.close();
  }
} 