public class Problem_11_1{
    public static void main(String[] args) {
        int number = 12345;
        int count = 0;
        
         while(number > 0){
        number/=10;
        count++;
    }  
        System.out.println(count);

        }

    }
