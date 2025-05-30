import java.util.Arrays;
public class LS_03 {
    public static void main(String[] args) {
        
        int arr[] = {10 ,20, 30  , 40, 50};
        System.out.println(Arrays.toString(arr));

        int min = findMin(arr);
        System.out.println("Min:"+ min);

    }
    private static int findMin(int arr[]){
        int min = arr[0];
        for(int i=0; i<arr.length; i++){
            if(arr[i] < min){
                min = arr[i];
            }
        }
        return min;
    }
}
