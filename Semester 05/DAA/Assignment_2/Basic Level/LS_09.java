import java.util.Arrays;
public class LS_09 {

    public static void main(String[] args) {
        
        String arr [] = {"hello"};
        char ch = 'h';
        int x = find(arr , ch);
        System.out.println("Char fount  :"+x);
    }
    private static int find(String arr [] , char ch){
        for(int i = 0; i < arr.length; i++){
            if(arr.charAt(i) == ch){
                return i;
            }
        }
        return -1;

    }
}