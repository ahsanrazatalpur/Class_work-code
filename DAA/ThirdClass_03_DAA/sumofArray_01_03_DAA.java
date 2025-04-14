public class sumofArray_01_03_DAA{
    public static void main(String args []){
        int [] marks = {23, 45, 67, 87};
        int digit = 0;
        int sum = 0;
         
        while(marks > 0){
        digit = marks % 10;
        sum += digit;
        //marks /= 10;
        System.out.print(sum);

    }

}
}