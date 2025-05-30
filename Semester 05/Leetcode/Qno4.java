public class Qno4 {

    public static void main(String[] args) {
        int[] nums1 = {1, 3};
        int[] nums2 = {2};

        double median = findMedianSortedArrays(nums1, nums2);  // call static method
        System.out.println("Median of merged sorted arrays: " + median);
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] ans = merge(nums1, nums2);
        if (ans.length % 2 == 0) {
            return (double)(ans[ans.length / 2] + ans[ans.length / 2 - 1]) / 2;
        } else {
            return (double)(ans[ans.length / 2]);
        }
    }

    public static int[] merge(int[] arr1, int[] arr2) {
        int[] ans = new int[arr1.length + arr2.length];
        int p1 = 0, p2 = 0, p3 = 0;

        while (p1 < arr1.length || p2 < arr2.length) {
            int val1 = p1 < arr1.length ? arr1[p1] : Integer.MAX_VALUE;
            int val2 = p2 < arr2.length ? arr2[p2] : Integer.MAX_VALUE;

            if (val1 < val2) {
                ans[p3++] = val1;
                p1++;
            } else {
                ans[p3++] = val2;
                p2++;
            }
        }
        return ans;
    }
}
