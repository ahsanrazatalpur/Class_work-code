import java.util.Arrays;
public class LS_05 {

    public static void main(String[] args) {
        
        int arr[] = {1, 2 ,3, 4, 2, 6, 2};
        System.out.println(Arrays.toString(arr));
        int x = find(arr, 2);
         System.out.println("The ocurence of array are :" +x);
        
        
        
    }
    private static int find(int [] arr, int x){
        int count = 0;
        for(int i= 0; i <arr.length; i++){

            if(arr[i] == x){
                count++;
                
            }
        }
        return count ;
         
    }
}