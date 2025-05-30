import java.util.Arrays;
public class LS_01{
public static void main(String[] args) {
    
    int arr [] = {10 , 20 , 30 , 40 , 50};
    System.out.println(Arrays.toString(arr));
    int x = find(arr , 30);
    System.out.println("Element Found at index:"+x);
}
private static int find(int [] arr , int x){
for(int i=0; i<arr.length-1; i++){
    if(arr[i] == x){
        return i;
    }
    
}
return -1;
}
}

