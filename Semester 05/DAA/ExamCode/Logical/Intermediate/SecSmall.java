import java.util.Arrays;
public class SecSmall {
    public static void main(String[] args) {

        int arr[] = {10 ,20, 30, 40, 50};
        System.out.println(Arrays.toString(arr));

        int secmin = secMin(arr);
        System.out.println("SecoundMin :"+secmin);
        
    }
    private static int secMin(int arr[]){
        if(arr.length < 2){
            System.out.println("Array must be greater than 2");
        }
        int min1,min2;
        if(arr[0] < arr[1]){
            min1 = arr[0];
            min2 = arr[1];
        }
        else{
            min1 = arr[1];
            min2 = arr[2];
        }
        for(int i=2; i<arr.length; i++){
            if(arr[i] < min1){
                min2 = min1;
                min1 = arr[i];
            }
            else if(arr[i] < min2 && arr[i] != min1){
            
            }
        }
        return min2;
    }
    
}
