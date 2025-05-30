import java.util.Arrays;
public class LS_04{
    public static void main(String[] args) {
    
        int arr[] = {10 ,20 ,30, 40, 50};
        System.out.println(Arrays.toString(arr));
        int x = find(arr, 40);
        System.out.println("Found :"+ x);
    }
    private static int find(int arr[], int x){
        for(int i=0; i<arr.length; i++){
            if(arr[i] == x){
                return x;
            }
        }
        return -1;
    }
}