import java.util.Random;
public class ArrayData{
	  public double[] array=new double[100000];
	  private int arrl=0;
	  public ArrayData(double[] A){
		  for(int i=0;i<A.length;++i){
			  array[i]=A[i];
			  arrl++;
		  }
	  }
	  public double max(){
		  double max=array[0];
		  for(int i=1;i<arrl;++i){
			  if(array[i]>max) max=array[i];
		  }
		  return max;
	  }
	  public double avg(){
		  double avg=0;
		  for(int i=0;i<arrl;++i){
			  avg+=array[i];
		  }
		  return (avg/arrl);
	  }
	  public void reverse(){
		  double tmp;
		  for(int i=0;i<(arrl/2);++i){
			  tmp=array[i];
			  array[i]=array[arrl-1-i];
			  array[arrl-1-i]=tmp;
		  }
	  }
	  public void shuffle(){
		  Random ran = new Random();
		  double tmp;
		  for(int i=0;i<(arrl/2);++i){
			  int ri=ran.nextInt(arrl);
			  tmp=array[i];
			  array[i]=array[ri];
			  array[ri]=tmp;
		  }
	  }
	  public String toString(){
		  String s="";
		  String tmp="";
		  for(int i=0;i<arrl;++i){
			  tmp=array[i]+" ";
			  s+=tmp;
		  }
		  return s;
	  }
	  public double inner_product(double[] B){
		  double sum=0.0;
		  for(int i=0;i<arrl;++i){
			  sum+=array[i]*B[i];
		  }
		  return sum;
	  }
  }