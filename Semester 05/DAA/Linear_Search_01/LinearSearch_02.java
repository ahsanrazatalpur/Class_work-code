import java.util.Arrays;
public class LinearSearch_02 {
    public static void main(String[] args) {
        //There are Three way to create an array

        // First way to create an array
        int arr[] = new int [5];

        //Second way to create an array
        int arr2 [];
        arr2 = new int [5];

        //third way to craete an array
        int arr3[] = {10, 33, 66, 77};


        // Three way to print an array
        // first way to print an array
        for(int i=0; i<arr3.length; i++){
            System.out.println(arr3[i]);
        }
        
        //Second way to print an array
        for(int number : arr3){
            System.out.println(number);
        }

        //third way to print an array
        System.out.println(Arrays.toString(arr3));


    }
}
