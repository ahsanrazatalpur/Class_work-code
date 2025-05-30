import java.util.Arrays;
public class LS_04 {
    public static void main(String[] args) {
        
        int arr[] = {10 ,20, 30, 40, 50};
        System.out.println(Arrays.toString(arr));
        
        reverse(arr);
        System.out.println(Arrays.toString(arr));
    }
    private static void reverse(int arr[]){
        int start = 0;
        int end = arr.length-1;

        while(start < end){
            swap(arr, start, end);
                start++;
                end--;
            
        }

    }
    private static void  swap(int arr[] , int start, int end){
        int temp = 0;
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
    }

}

