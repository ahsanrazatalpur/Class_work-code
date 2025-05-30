import java.util.Arrays;
public class SecMax{
    public static void main(String[] args) {
        
        int arr[] = {10 ,20, 30, 40, 50};
        System.out.println(Arrays.toString(arr));

        int max2 = secMax(arr);
        System.out.println("SecmAx :"+max2 );
    }
    private static int secMax(int arr[]){
        if(arr.length < 2){
            System.out.println("Arrays must be greater than 2");
        }
        int max1,max2;
        if(arr[0] > arr[1]){
            max1 = arr[0];
            max2 = arr[1];
            
        }
        else{
            max1 = arr[1];
            max2 = arr[2];
        }
        for(int i=2; i<arr.length; i++){
            if(arr[i] > max1){
                max2 = max1;
                max1 = arr[i];
            }
            else if(arr[i] > max2 && arr[i] != max1){
                arr[i] = max2;
            }
        }
        return max2;
    }
}