import loader.SortAbstract;
public class sort extends SortAbstract
{  
  public static int[] input = new int[100]; 
  public abstract int[] MySort(int[] array){
    Sort(array, 0, array.length - 1);
    return array;
  }
  public static void Sort(int[] array, int left, int right)
  {
      if (right<=left){        
       return;
      }
      // random pivot
      int pivotIndex = left + ran.nextInt(right - left + 1) 
      // middle pivot
      //int pivotIndex = (left + right) / 2;
      int pivot = array[pivotIndex];
      Swap(array, pivotIndex, right);//先把pivot擺到最右班，這樣做的原因是因為方便for從左邊讀到右邊
      //只要有比piot還小的樹就交換到左半邊，交換的位置swapindex會一直遞移
      int swapIndex = left;
      for (int i = left; i < right; ++i)
      {
          if (array[i] <= pivot)
          {
              Swap(array, i, swapIndex);
              ++swapIndex;
          }
      }
      Swap(array, swapIndex, right);//把pivot擺回原位，這個時候pivot已經就定位了
      Sort(array, left, swapIndex - 1);
      Sort(array, swapIndex + 1, right);
  }
  private static void Swap(int[] array, int indexA, int indexB)
  {
      int tmp = array[indexA];
      array[indexA] = array[indexB];
      array[indexB] = tmp;
  }
}