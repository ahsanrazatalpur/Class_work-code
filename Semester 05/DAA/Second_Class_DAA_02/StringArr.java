import java.util.Scanner;
public class StringArr {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Enter the  size of an array");
        int size = in.nextInt();

        String arr[] = new String [size];
        
        System.out.println("Enter string :");
        for(int i=0; i<size; i++){
            arr[i] = in.nextLine();


        }
        for(int i=0; i<size; i++){
        System.out.println(arr[i]);
        }
        
    }
}
