public class Qno69 {
    public static void main(String[] args) {
        int arr[] = {12 ,35 ,67 ,78, 89, 90};
        System.out.println(ceilingFunction(arr,66));
    }
    private static int ceilingFunction(int []arr,  int target){
        int start = 0;
        int end = arr.length-1;
        while(start <= end){
            int mid = start + (end - start)/2;
            if(target > arr[mid]){
                start = mid + 1;
            }
            else{
                if(target < arr[mid]){
                    end = mid - 1;
                }
                else{
                    return mid;
                }
            }
        }
        return arr[start];  // for value
        // return start; for index
    }
    
}

    

