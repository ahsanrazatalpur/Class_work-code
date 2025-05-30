public class Array_01{
    public static void main(String[] args) {
        
        // Array is collection of same type of data
        //There are three way to demostrate the array

        //First way to declare and print an array
        int arr [] = new int [5];

        // assigning value
        arr[0] = 10;
        arr[1] = 20;
        arr[2] = 30;
        arr[3] = 40;
        arr[4] = 50;
        
        //Printing array
        System.out.println(arr[0]);
        System.out.println(arr[1]);
        System.out.println(arr[2]);
        System.out.println(arr[3]);
        System.out.println(arr[4]);
        
        System.out.println();
    
        // 2nd way to demonsrate an aray
        int arr2 [];
        arr2 = new int [5];

        arr[0] = 100;
        arr[1] = 200;
        arr[2] = 300;
        arr[3] = 400;
        arr[4] = 500;

        // printing array in loop
        for(int i=0; i<arr2.length; i++){
            System.out.println(arr[i]);
        }
        System.out.println();
        
        // 3rd way to demonstrate an array
        
        int arr3 [] = {1000, 2000, 3000, 4000, 5000};
        
        //printing an array
        for(int i=0; i<arr3.length; i++){
            System.out.println(arr3[i]);
        }
        System.out.println();


    }
}