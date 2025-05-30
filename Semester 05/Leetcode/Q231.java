public class Q231 {

    public static void main(String[] args) {
        int n = 16;

        boolean result = isPowerOfTwo(n);  
        System.out.println(n + " is a power of two: " + result);
    }

    public static boolean isPowerOfTwo(int n) {
        if (n < 1) {
            return false;
        } else if (n == 1) {
            return true;
        } else {
            while (n % 2 == 0) {
                n = n / 2;
            }
            return n == 1;
        }
    }
}
