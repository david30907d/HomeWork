package hw01;
import java.util.*;
import loader.Algorithm3SumFastest;
public class Threesum extends Algorithm3SumFastest
{	
	public int count(int[] arr){
		int num_of_threesum=0;
		Arrays.sort(arr);
		for(int i=0;i<arr.length-2;++i){
			int start=i+1;
			int end=arr.length-1;
			int x=arr[i];
			while(start<end){
				if(x+arr[start]+arr[end]<0){
					start++;
				}
				else if (x+arr[start]+arr[end]>0) {
					end--;
				}
				else{
					num_of_threesum++;
					start++;//因為題目規定數列的每個數都是不同的，所以才可以start跟end都互相靠近，若數列會有重複題目要重複計算的話，end---和start++只能保留一項
					end--;
				}
			}
		}
		return num_of_threesum;
	}
	public static void main(String[] args) {
		
	}
}
