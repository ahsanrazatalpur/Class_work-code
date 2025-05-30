public class Problem_704{
    public static void main(String[] args) {
        int arr[] = {1 ,2 ,3, 4, 5};
        int x = find(arr,3);
        System.out.println("Traget :"+x);
    }
    private static int find(int arr[], int x){
        int start = 0;
        int end = arr.length-1;

        while( end >= start){
            int mid  = start + (end - start)/2;
            if(x > arr[mid])
            start = mid + 1;
            else
            if(x < arr[mid]){
                end = mid - 1;
            }
            else 
             return mid;

        }
        return -1;

    }
}