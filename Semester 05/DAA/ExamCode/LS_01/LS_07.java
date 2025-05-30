import java.util.Arrays;
public class LS_07 {
    public static void main(String[] args) {
        
        int arr[] = {10, 20 ,30 , 49};
        System.out.println(Arrays.toString(arr));

        int max = findMax(arr);
        System.out.println("Max :"+max);
    }
    private static int findMax(int arr[]){
        int max = arr[0];
        for(int i=0; i<arr.length; i++){
            if(arr [i] > max){
                max = arr[i];
            }
        }
        return max;
    }
    
}
