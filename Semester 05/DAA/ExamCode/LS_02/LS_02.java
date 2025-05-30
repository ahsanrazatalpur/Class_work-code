public class LS_02{
    public static void main(String[] args) {
        
        int arr[][] = {
            {10, 20, 30, 40 ,50},
            {5, 10, 150, 20, 25},
            {20 ,40 ,60, 80, 100}

        };
            System.out.println(max(arr));
    }
    private static int max(int arr[][]){
        int max = arr[0][0] ;
        for(int row=0; row<arr.length; row++){
            for(int col = 0; col < arr[row].length; col++){
                if(arr[row][col] > max){
                    max = arr[row][col];
                }
            }
            

        }
        return max;
    }
}