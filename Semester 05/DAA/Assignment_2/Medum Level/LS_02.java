public class LS_02 {
    public static void main(String[] args) {
        int arr[] = {10, 20, 30, 40, 50};
        int min = arr[0];
        int secmin = Integer.MAX_VALUE;
        int x = find(arr, secmin, min);
        System.out.println("The second smallest element is: " + x);
    }

    private static int find(int arr[], int secmin, int min) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                secmin = min;
                min = arr[i];
            } else if (arr[i] < secmin && arr[i] != min) {
                secmin = arr[i];
            }
        }
        return secmin == Integer.MAX_VALUE ? -1 : secmin;
    }
}

