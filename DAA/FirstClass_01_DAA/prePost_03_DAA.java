public class prePost_03_DAA{
    public static void main(String args[]){
        // i++   post increament
        // ++i   pre increament
        int i = 0;
        i = 5;
        i++;
        System.out.println(i+" ");

        int j = 5;
        ++j;
        System.out.println(j+" "); 

        int k = 5;
        System.out.println("Post increament :"+k++); // here post inc value change but show or print in next step(value is assign but show in next step)
        System.out.println(k);

        int m = 5;
        System.out.println("pre Increment :" + ++m); // value change and print in same line or step
        System.out.println(m);

    
    }
}