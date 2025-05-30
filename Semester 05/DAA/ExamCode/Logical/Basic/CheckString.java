public class CheckString {
    public static void main(String[] args) {
        
        String greet = "Hello";

    int ch = find(greet,'o');
        System.out.println("Char found at index :"+ch);

    }
    private static int find(String greet, char ch){
        for(int i=0; i<greet.length(); i++){
            if(greet.charAt(i) == ch){
                return i;
            }
        }
        return -1;
    }
    
}
