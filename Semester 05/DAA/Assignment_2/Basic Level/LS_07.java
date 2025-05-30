public class LS_07 {

    public static void main(String[] args) {
        
        int arr [] = {12 , 45, 67, 78};
        int min = arr[0];

        int x = find(arr,min);
        System.out.println("Min :"+x);
    }
    private static int find(int arr[] , int min){
        for(int i=1; i<arr.length; i++){
            if(min > arr[i]){
                min = arr[i];
            }
        }
        return min;
    }
}