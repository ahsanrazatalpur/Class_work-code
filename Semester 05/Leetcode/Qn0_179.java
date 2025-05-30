import java.util.Arrays;
public class Qn0_179 {

    public String largestNumber(int[] nums) {
        String[] arr = new String[nums.length];

        for(int i = 0; i < nums.length; i++){
            arr[i] = nums[i] + "";
        }

        // Sort with custom comparator, s1+s2 vs s2+s1
        Arrays.sort(arr, (s1, s2) -> (s1 + s2).compareTo(s2 + s1));
        
        StringBuilder sb = new StringBuilder();

        // Append in reverse order for descending concatenation
        for(int i = arr.length - 1; i >= 0; i--){
            sb.append(arr[i]);
        }

        // Handle leading zero case
        if(sb.charAt(0) == '0'){
            return "0";
        } else {
            return sb.toString();
        }
    }

    // Testing in main
    public static void main(String[] args) {
        Qn0_179 sol = new Qn0_179();  // Create instance
        int[] nums = {3, 30, 34, 5, 9};
        String largestNum = sol.largestNumber(nums);
        System.out.println("Largest Number: " + largestNum);
    }
}
