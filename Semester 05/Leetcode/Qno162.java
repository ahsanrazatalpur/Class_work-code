public class Qno162 {
    public static int findPeakElement(int[] nums) {   // made static
        if(nums.length == 1) {
            return 0;
        } else if (nums[0] > nums[1]) {
            return 0;
        } else if (nums[nums.length - 1] > nums[nums.length - 2]) {
            return nums.length - 1;
        } else {
            int start = 1;
            int end = nums.length - 2;
            while(start <= end) {
                int mid = (start + end) / 2;
                if(nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) {
                    return mid;
                } else if(nums[mid] < nums[mid + 1]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
            return -1;
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 3, 20, 4, 1, 0};

        // Now you can call the method directly without creating an object
        int peakIndex = findPeakElement(nums);

        System.out.println("Peak element index: " + peakIndex);
        System.out.println("Peak element value: " + nums[peakIndex]);
    }
}
