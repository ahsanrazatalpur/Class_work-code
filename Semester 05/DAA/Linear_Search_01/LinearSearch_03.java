import java.util.Arrays;
public class LinearSearch_03{
    public static void main(String args []){
        
        int arr[] = {10, 20, 20, 38};
        System.out.print(Arrays.toString(arr));
        
        reverse(arr);
        System.out.println(Arrays.toString(arr));
        
        
        
    }
    private static void reverse(int arr[]){
        int start = 0;
        int end = arr.length-1;
        
        while(start < end){
            swap(arr, start, end);
            start++;
            end --;
        }
    }
    private static void swap(int arr[] ,int start, int end){
        int temp = 0;
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
    }
    }

