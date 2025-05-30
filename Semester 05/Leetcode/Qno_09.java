public class Qno_09 {
    public static void main(String[] args) {
        
        int x = 123;
        int d = 0;
        int rev = 0;
        int n = x; 

        while (x > 0) {
            d = x % 10;
            rev = rev * 10 + d;
            x /= 10;
        }

        if (rev == n) {
            System.out.println("Is Palindrome");
        } else {
            System.out.println("Not Palindrome");
        }
    }
}
