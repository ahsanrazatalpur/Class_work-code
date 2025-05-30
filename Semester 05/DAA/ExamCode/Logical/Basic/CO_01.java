import java.util.Arrays;
public class CO_01{
    public static void main(String[] args) {
        
        int arr[] = {10 ,20, 30, 20, 40};
        System.out.println(Arrays.toString(arr));

        int x = countOccurence(arr, 20);
        System.out.println("Occurence Are :"+x);

    }
    private static int countOccurence(int arr[], int x){
        int count = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i] == x){
                count ++;
            }
        }
        return count;
    }
}