package hw01;
import loader.TrashCanAb;
public class queue extends TrashCanAb
{
	private String str;
	public queue(){
		str="";
	}
	public void Insert(int garbage) {
		str+=garbage+",";
	}
	public void Empty() {
		str="";
	}
	public String ToString() {
		String ans="";
		if(str.length()>=1){
			int len=str.length()-1;
			ans=str.substring(0, len);
		}
		ans="["+ans+"]";
		return ans;
	}
	public static void main(String[] args)	{
		
	}
}