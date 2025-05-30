
public class LS_08 {
    public static void main(String[] args) {
        
        int arr[] = {10 ,20 ,30 ,40 ,50};
        int x = find(arr, 60);
        System.out.println("Element not found :"+x);
    }
    private static int find(int arr[] , int x){
        for(int i = 0; i< arr.length; i++){
            if(x == arr[i]){
                return x;
            }
        }
        return 0;
    }
}
