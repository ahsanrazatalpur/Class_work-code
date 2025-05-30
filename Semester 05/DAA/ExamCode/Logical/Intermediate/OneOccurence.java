import java.util.Arrays;

public class OneOccurence {
    public static void main(String[] args) {
        int arr[] = {10, 20, 10, 40, 10, 70};
        System.out.println("Array: " + Arrays.toString(arr));

        int occur = findOneOccurrence(arr);
        if (occur != -1) {
            System.out.println("First element that occurs only once is: " + occur);
        } else {
            System.out.println("No element occurs exactly once.");
        }
    }

    private static int findOneOccurrence(int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            int count = 0;  // Reset count for each i
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    count++;
                }
            }
            if (count == 1) {
                return arr[i]; // Return the element itself
            }
        }
        return -1; // No unique element found
    }
}
