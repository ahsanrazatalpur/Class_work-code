public class LS_02 {
    public static void main(String[] args) {
        
        //There Are Three way to demonstrate an array

        // 1st way to create and print an array
        int arr[] = new int [5];

        arr[0] = 10;
        arr[1] = 20;
        arr[2] = 30;
        arr[3] = 40;
        arr[4] = 50;

        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);
        System.out.println(arr[3]);
        System.out.println(arr[4]);

        System.out.println();

        //2nd way to create an array
     String arr2[];
     arr2 = new String [5];

     arr2[0] = "Ali";
     arr2[1] = "Ahsan";
     arr2[2] = "Gull";
     arr2[3] = "Ayaz";
     arr2[4] = "Hammad";

     for(int i=0; i<arr2.length; i++){
        System.out.println(arr2[i] +" ");
     }

     System.out.println();

     // 3rd way to demonstrate an array 

     int arr3 [] = {100, 200, 300, 400, 500} ;
     for(int i=0; i<arr3.length; i++){
        System.out.println(arr3[i]);
     }
        
    }
    
}
