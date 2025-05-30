import java.util.Arrays;
public class CheckElement {
    public static void main(String[] args) {
        
        int arr[] = {10 ,20 ,30, 40 ,50};
        System.out.println(Arrays.toString(arr));

        int result = find(arr, 60);
        
        if(result == -1){
            System.out.println("Element not found");
        }
        else{
            System.out.println("Eleemnt found "+result);
        }
    }
    private static int find(int arr[] , int element){
        for(int i=0; i<arr.length; i++){
            if(arr[i] == element){
                return element;
            
        }
        
    }
    return -1;
    

    }}