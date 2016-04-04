package loader;

public abstract class TrashCanAb
{
	public abstract void Insert(int garbage);
	public abstract void Empty();
	public abstract String ToString();
	//垃圾桶有東西，回傳的String先進先出：[1,2,3]
	//垃圾桶為空，回傳的String長這樣：[]
}