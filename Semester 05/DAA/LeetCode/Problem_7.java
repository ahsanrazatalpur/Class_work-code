public class Problem_7 {
    public static void main(String[] args) {
        long n = 1534236469;
        long reverse = reverse(n);
        System.out.println("Reversed number: " + reverse);
    }

    private static long reverse(long n) {
        long reverse = 0;
        while (n != 0) {
            long digit = n % 10;
            reverse = reverse * 10 + digit;
            n /= 10;
        }
        return reverse;
    }
}
