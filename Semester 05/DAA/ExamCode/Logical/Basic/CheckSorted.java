import java.util.Arrays;
public class CheckSorted{
public static void main(String[] args) {
    
    int arr[] = {10, 20, 30, 40  ,50};
    System.out.println(Arrays.toString(arr));

    if(isSorted(arr)){
        System.out.println("Array is sorted :)");
    }
    else{
        System.out.println("Element is not Sorted :(");
    }

}
private static boolean isSorted(int arr[]){
    boolean isAscending = true;
    boolean isDescending = true;
    for(int i=0; i<arr.length-1; i++){
        if(arr[i] > arr[i + 1]){
            isAscending = false;
        }
        if(arr[i] < arr[i + 1]){
            isDescending = false;
        }
    }
    return isAscending | isDescending;
}
}