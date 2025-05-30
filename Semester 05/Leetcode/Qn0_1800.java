import java.util.Arrays;
public class Qn0_1800 {

    public static int maxAscendingSum(int[] nums) {  // 
        System.out.println("Input array: " + Arrays.toString(nums));

        int max = findMax(nums);
        System.out.println("Max: " + max);

        return max;
    }

    private static int findMax(int[] arr) {
        int max = arr[0];
        for(int i = 1; i < arr.length; i++) {
            if(arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }

    public static void main(String[] args) { 
        int[] nums = {10, 20, 30, 40, 50};
        int result = maxAscendingSum(nums);  // Now this works
        System.out.println("Result: " + result);
    }
}
