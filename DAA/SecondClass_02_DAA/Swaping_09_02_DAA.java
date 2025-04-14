public class Swaping_09_02_DAA{
    public static void main(String args[]){
        int a = 5;
        int b = 8;
        int temp = 0;

        temp = a;
        a = b;
        b = temp;

        System.out.println("The Value of an a after swaping :"+a);
        System.out.println("The value of b after swaping : "+b);
    }
}