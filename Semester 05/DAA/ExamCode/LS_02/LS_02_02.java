public class LS_02_02 {
    public static void main(String[] args) {
        int arr[][] = {
            {1, 2, 3, 4, 5},
            {5, 10, 15, 20},
            {12, 45, 46, 67}
        };
        System.out.println(min(arr));
    }
    private static int min(int arr[][]){
        int min = arr[0][0];
        for(int row=0; row<arr.length; row++){
            for(int col=0; col<arr[row].length; col++){
                if(arr[row][col] < min){
                    min = arr[row][col];
                }
            }
        }
        return min;
    }
    
}
