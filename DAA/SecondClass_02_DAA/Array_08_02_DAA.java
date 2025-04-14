import java.util.Scanner;
public class Array_08_02_DAA{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);

        System.out.println("Enter the size of an array");
        int size = in.nextInt();

        String names[] = new String[size];
        
        for(int i=0; i<names.length; i++){
        System.out.println("Enter a name: ");
        names[size] = in.nextLine();
        }

        for(int i=0; i<names.length; i++){
            System.out.println("Name : "+names[i]);
        }
    }
}