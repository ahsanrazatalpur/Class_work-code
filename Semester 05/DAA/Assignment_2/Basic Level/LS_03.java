import java.util.Arrays;
public class LS_03 {
    public static void main(String[] args) {

        int arr[] = {10, 20, 30, 20 ,40};
        System.out.println(Arrays.toString(arr));

        int x = find(arr,20);
        System.out.println("Last ocuurence at index :" +x);
    }
    private static int find(int arr[], int x){
        for(int i=arr.length-1; i>=0; i--){
            if(arr[i] == x){
                return i;
            }
        }
        return -1;
    }
}
