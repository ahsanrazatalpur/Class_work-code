public class LS_08{
    public static void main(String[] args) {
        
        String str = "Pakistan";
        boolean b = find(str, 'y');
        System.out.println("Found y : "+b);
    }
    private static boolean find(String str , char x){
        if(str.length() == 0){
            return false;
        }
        else{
            for(char i :str.toCharArray()){
                //if(i == x){
                    return true;
              //  }
            }
        }
        return false;
    }
}