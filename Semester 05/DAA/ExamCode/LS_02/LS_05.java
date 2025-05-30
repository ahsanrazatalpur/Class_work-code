import java.util.Arrays;
public class LS_05 {
    public static void main(String[] args) {
        
        int arr[][] = {
            {10, 20, 30, 40},
            {100, 300 ,400 ,500},
            {23, 45, 67, 68}
        };

        int x [] = find(arr , 300);
        System.out.println("Found at"+ Arrays.toString(x));
        
    }
    private static int find(int arr[][], int x){
        for(int row=0; row<arr.length; row++){
            for(int col=0; col<arr[row].length; col++){
                if(arr[row][col] == x){
                    return new int []{row,col};
                }
            }
        }
    }
    return new int[]{-1,-1};

}
