public class Problem_287 {
    public static void main(String[] args) {
    
        int arr[] = {1, 2, 3, 2, 1};
        int x = find(arr);
        System.out.println("Index of peak element: " + x);
        
    }
    
    private static int find(int arr[]){
        int max = arr[0];  
        int index = 0;  
        
        for(int i = 1; i < arr.length; i++){  
            if(arr[i] > max) {
                max = arr[i];  
                index = i;   
            }
        }
        
        return index;  
    }
}
