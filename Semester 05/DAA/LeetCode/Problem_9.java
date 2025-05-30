public class Problem_9 {
    public static void main(String[] args) {
        int x = 121;
        boolean isPalindrome = isPalindrome(x);
        System.out.println(isPalindrome);
    }

    public static boolean isPalindrome(int x) {
        int n = x;
        if (n < 0) {
            return false;
        }

        int rev = 0;

        while (n > 0) {
            int digit = n % 10;
            rev = rev * 10 + digit;
            n /= 10;
        }

        return rev == x;
    }
}
