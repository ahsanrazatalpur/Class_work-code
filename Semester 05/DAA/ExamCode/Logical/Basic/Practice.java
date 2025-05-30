public class Practice {
    public static void main(String[] args) {
        int arr[]={1,2,2,2,3,4};
        int target=2;
        int startPosition=startPosition(arr);
        int endPosition=endPosition(arr);
    }
    private static int startPosition(int arr[],int target){
        int start=0;
        int end=arr.length;
        int result=0;
        while (start<end) {
            int mid=start+(end-start)/2;
            if(target==arr[end]){
                result=mid;
                end=mid-1;
            }
            else if(target>arr[mid])
                

        }
    }
}
