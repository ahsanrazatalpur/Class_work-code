import java.util.Scanner;
public class Array_07_02_DAA{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Enter marks: ");
        int marks[] = new int[3];

        for(int i=0; i<marks.length; i++){
            marks[i] = input.nextInt();
        }
        for(int i=0; i<marks.length; i++){
            System.out.println("Marks :"+marks[i]);
        }
    }
}