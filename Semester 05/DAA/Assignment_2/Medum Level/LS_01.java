public class LS_01 {
    public static void main(String[] args) {
        int arr[] = {10, 20, 30, 40, 50};
        int max = arr[0];
        int secmax = Integer.MIN_VALUE;
        int x = find(arr, secmax, max);
        System.out.println("The second largest element is: " + x);
    }

    private static int find(int arr[], int secmax, int max) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                secmax = max;
                max = arr[i];
            } else if (arr[i] > secmax && arr[i] != max) {
                secmax = arr[i];
            }
        }
        return secmax == Integer.MIN_VALUE ? -1 : secmax;
    }
}
