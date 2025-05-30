public class Problem_268 {

    public static void main(String[] args) {
        int[] nums = {3, 0, 1};  // Example: missing number is 2
        Problem_268 obj = new Problem_268();
        int result = obj.missingNumber(nums);
        System.out.println("Missing number: " + result);
    }

    public int missingNumber(int[] nums) {
        int range = nums.length;
        int actualsum = (range * (range + 1)) / 2;

        int currentsum = 0;
        for (int i = 0; i < nums.length; i++) {
            currentsum += nums[i];
        }

        int ans = actualsum - currentsum;
        return ans;
    }
}
