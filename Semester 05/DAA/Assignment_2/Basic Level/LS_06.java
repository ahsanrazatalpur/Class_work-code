import java.util.Arrays;
public class LS_06 {

    public static void main(String[] args) {
        
        int arr [] = {23, 5, 100, 23, 68};
        System.out.println(Arrays.toString(arr));
       
        int max = arr[0];
        int x = find(arr, max);
        System.out.println("Max :"+x);
    }
    private static int find(int arr[], int max){
        for(int i=0; i<arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
            }
        }
        return max;
    }
}