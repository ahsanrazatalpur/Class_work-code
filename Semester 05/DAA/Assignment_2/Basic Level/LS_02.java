import java.util.Arrays;
public class LS_02 {
    public static void main(String[] args) {
        int arr[] = {1, 3, 5, 6};
        System.out.println(Arrays.toString(arr));

        int x = find(arr,5);
        System.out.println("First occurence at index :"+x);
        
    }
    private static int find(int arr[] , int x){
        for(int i=0; i<arr.length; i++){
            if(arr[i] == x){
                return i;
            }
        }
        return -1;
    }
}
