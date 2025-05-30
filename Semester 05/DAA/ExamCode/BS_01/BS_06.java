public class BS_06 {
    public static void main(String[] args) {
        
        char letter[] = {'a', 'b', 'd'};
        System.out.println(floorChar(letter, 'c'));
    }
    private static char floorChar(char letter[],char target ){
        int start = 0;
        int end = letter.length-1;
        while(start <= end){
            int mid = start + (end - start)/2;
            if(target > letter[mid]){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
        }
        if(start == letter.length ){
            return letter[0];
        }
        else{
            return letter[end];
        }
    }
    
}
