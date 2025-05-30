import java.util.Arrays;
public class LinearSearch_01 {

    public static void main(String[] args) {
        
     int arr [] = {10, 20, 30 ,40, 50};
     System.out.println(Arrays.toString(arr));

     int sum = add(arr);
     System.out.println("Sum :"+sum);
     
    }
     static int add(int [] arr2){
        int x = 0;
        for(int i=0; i<arr2.length; i++){
            x += arr2[i];
        }
return x;
    }
}
______________________________________________________________