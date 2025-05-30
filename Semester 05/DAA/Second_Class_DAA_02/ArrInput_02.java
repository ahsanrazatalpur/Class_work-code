import java.util.Scanner;
public class ArrInput_02 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter The size of an array :");
        int size = in.nextInt();

        int arr[] = new int [size];

        System.out.println("Enter "+size+" integer");
        for(int i=0; i<size; i++){
            arr[i] = in.nextInt();
        }

        for(int i=0; i<size; i++){
            System.out.println(arr[i]);
        }


    }
}