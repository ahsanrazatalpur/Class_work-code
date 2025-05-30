import java.util.Scanner;
public class printTable{
    public static void main(String args[]){
        
        Scanner in = new Scanner(System.in);
        System.out.print("Enter The number of table :");
        int tableof = in.nextInt();

        for(int i=1; i<=10; i++){
            System.out.println(tableof + "X" + i+ "=" +i*tableof);
        }
    }
}