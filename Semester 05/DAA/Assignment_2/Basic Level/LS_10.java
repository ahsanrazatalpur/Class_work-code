import java.util.Arrays;
public class LS_10 {
    public static void main(String[] args) {
        
        int arr [] = {1, 2, 4 , 6, 7};
        int x = find(arr);
        System.out.println("Array is sorted :"+x);
    }
    private static int find(int arr[], int x ){
        for(int i=0; i<arr.length; i++){
            if(arr[0] > arr[arr.length-1]){
                return x;
            }
        }
        System.out.print("Array is not sorted ");
    }
}
