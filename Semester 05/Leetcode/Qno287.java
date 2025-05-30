public class Qno287 {
    

    // Method to find any duplicate number using two loops
    public int findDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return nums[i]; // Duplicate found
                }
            }
        }
        return -1; // No duplicate found
    }

    public static void main(String[] args) {
        Qno287 solution = new Qno287();

        int[] nums = {1, 3, 4, 2, 2};
        int duplicate = solution.findDuplicate(nums);

        if (duplicate != -1) {
            System.out.println("Duplicate number found: " + duplicate);
        } else {
            System.out.println("No duplicate found.");
        }
    }
}

    
