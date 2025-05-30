public class LS_09 {
    public static void main(String[] args) {
        
        boolean b = palindrome("abc");
        System.out.println(b);
    }
    private static boolean palindrome(String str){
        boolean b = true;
        for(int i=0; i<str.length()/2; i++){
            if(str.charAt(i) != str.charAt(str.length()-i-1)){
                b = false;
            }
        }
        return b;
    }
}
