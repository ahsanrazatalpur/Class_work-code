public class Problem_167 {

    public static void main(String[] args) {
        Problem_167 obj = new Problem_167();

        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        int[] result = obj.twoSum(numbers, target);

        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }

    public int[] twoSum(int[] numbers, int target) {
        int[] ans = new int[2];

        int start = 0;
        int end = numbers.length - 1;

        while (start <= end) {
            int sum = numbers[start] + numbers[end];

            if (sum == target) {
                ans[0] = start + 1;
                ans[1] = end + 1;
                return ans;
            } else if (sum > target) {
                end--;
            } else {
                start++;
            }
        }
        return ans;
    }
}
