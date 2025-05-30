import java.util.Arrays;
public class LS_04 {
    public static void main(String[] args) {
        
        int arr2D [][] = {
            {1, 2 ,3},
            { 4, 5, 6},
            {7, 8, 9}
        };

        int [] x = find(arr2D, 5);
        System.out.println("Found at :"+Arrays.toString(x));

    }
    private static int [] find(int arr2D[][],int x){
        for(int row = 0 ; row <arr2D.length; row++){
            for(int col = 0; col< arr2D[row].length; col++){
                if(arr2D [row][col] == x){
                    return new int [] {row, col};
                }
            }
        }
        return new int [] {-1 ,-1};
    }
}
