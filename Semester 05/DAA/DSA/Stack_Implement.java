// import java.util.Scanner;
// class stack{
//     int arr [] = new int [10];  // craete an array of 10 element
//     int top = -1;   // top initialay -1 because no element in starting

//     // push element for add an element
//     void push(){ 
//         if(top == arr.length-1){  // here we check overflow condition if top -1 that mean there is no element in stack
//             System.out.println("Overflow condition");
//         }
//         else{
//             System.out.print("Enter an Element : ");
//             int item = in.nextInt();
//             top = top + 1;  // one item added now incraese top 
//             arr[top] = item;
//             System.out.println("Item inserted :)");
//         }
//     }

//     // pop for remove top element
//     void pop(){ 
//         if(top == -1){ // top -1 mean no element in the stack
//             System.out.println("Underflow Condition"); 

//         }
//         else{
//             top -- ;
//             System.out.println("Item Deleted :( ");
//         }

//     }

//     // display  all item
//     void Display(){
//         System.out.println("Itemes are ");
//         for(int i=0; i<=top; i++){
//             System.out.println(arr[i]);

//         }
//     }

// }

// public class Stack_Implement {

//     public static void main(String[] args) {
        
//         Scanner in = new Scanner (System.in); 
//         stack s = new stack (); // craete an object for stack class

//         do{
//             System.out.println("Press 1 to Push");
//             System.out.println("Press 2 to Pop");
//             System.out.println("Press 3 to Display");
//             System.out.println("Enter your choice");
            
//             choice = in.nextInt();
//             switch(choice){
                
//                 case 1 :{
//                     s.push(in);
//                     break;
//                 }
//                 case 2 :{
//                     s.pop(in);
//                     break;
//                 }
//                 case 1 :{
//                     s.push(in);
//                     break;
//                 }
//             }
//             System.out.println("Enter 0 to go back main menu");
//             System.out.println("Enter any key to exit");
//             while(l == 0);
//             System.out.println("Exit Succesfully");
//         }
        
//         // Stack using array
//         //Operation are common in stack
//         // UnderFlow condition(stack is empty)
//         // OverFlow condition(stack is full)
//         // Push()
//         // Pop()
//         // Display()

// //intial value of stack top is -1    top = -1(mean there is no element in stack) <= underflow condition 
// // we check underflow condition if we want to delete an item
// // we check overflow condition if we want to add an item

// // push  =>  overflow condition
// // pop   =>  underflow conditionsss

// // top represent  index

// // push  top ++
// // pop  top --





//     }
// }