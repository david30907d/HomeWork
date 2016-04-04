import loader.QueueAb;
public class resizing_arr extends QueueAb
{  
  public int[] arr;
  private int size;
  private int ptr;
  public resizing_arr(){
    arr=new int[3];
    size=3;
    ptr=0;
  }
  public int[] resizeArray (int[] oldArray, int newSize) {
    // int oldSize = java.lang.reflect.Array.getLength(oldArray);
    Class elementType = oldArray.getClass().getComponentType();//可以拿到array的class類別
    Object newArray = java.lang.reflect.Array.newInstance(
    elementType, newSize);//建立新陣列size is newSize
    System.arraycopy(oldArray, 0, newArray, 0, newSize/2);//複製oldArray從index0開始，到newArray從index0開始，複製長度為prserveLength
    size=newSize;
    return (int[])newArray; 
  }
  public void Enqueue(int element){
    int newSize=size*2;
    if(ptr>=size){
        this.arr=this.resizeArray(arr,newSize);
    }
    arr[ptr++]=element;
  }
  public int Dequeue(){
    int shrink_val=size/4;
    if(ptr<=shrink_val){
      this.arr=this.resizeArray(arr,shrink_val*2);
    }   
    try{
      return arr[--ptr];
    }
    catch(Exception e){
      return 0;
    }
  }
  public static void main (String[] args) {
    resizing_arr r=new resizing_arr();
    r.Enqueue(56);
    r.Enqueue(100);
    r.Enqueue(10);
    r.Enqueue(1020);
    r.Enqueue(10330);
    for (int i=0; i<4; i++){
      System.out.println(r.arr[i]);
    }
    int test=r.Dequeue();
    System.out.println("test:"+test);
    test=r.Dequeue();
    System.out.println("test:"+test);
    
  }
}