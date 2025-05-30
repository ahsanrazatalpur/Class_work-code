import java.util.Arrays;
public class LS_05{
    public static void main(String[] args) {
        
        int arr[] = {10, 20, 30, 40, 50};
        System.out.println(Arrays.toString(arr));
        find(arr, 10);

    }
    private static void find(int arr[], int x){
        boolean b = false;
        for(int i=0; i<arr.length-1; i++){
            if(arr[i] == x){
                
                b = true;
                break;
            }
        }
        System.out.println(b? x + " : found " : x + "Not found");
    }
}