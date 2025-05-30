import java.util.Scanner;

class Stack {
    int arr[] = new int[10];
    int top = -1;

    void push(Scanner in) {
        if (top == arr.length - 1) {
            System.out.println("Overflow condition");
        } else {
            System.out.print("Enter an Element: ");
            int item = in.nextInt();
            top = top + 1;
            arr[top] = item;
            System.out.println("Item inserted :)");
        }
    }

    void pop() {
        if (top == -1) {
            System.out.println("Underflow Condition");
        } else {
            System.out.println("Item deleted: " + arr[top]);
            top--;
        }
    }

    void display() {
        if (top == -1) {
            System.out.println("Stack is empty");
        } else {
            System.out.println("Items are:");
            for (int i = 0; i <= top; i++) {
                System.out.println("Index " + i + ": " + arr[i]);
            }
        }
    }

    // ✅ Search function to find the index of an element
    void search(int element) {
        boolean found = false;
        for (int i = 0; i <= top; i++) {
            if (arr[i] == element) {
                System.out.println("Element " + element + " found at index " + i);
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("Element " + element + " not found in the stack.");
        }
    }
}

public class Stack2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Stack s = new Stack();
        int choice;
        int cont;

        do {
            System.out.println("\nPress 1 to Push");
            System.out.println("Press 2 to Pop");
            System.out.println("Press 3 to Display");
            System.out.println("Press 4 to Search for an element");
            System.out.print("Enter your choice: ");
            choice = in.nextInt();

            switch (choice) {
                case 1:
                    s.push(in);
                    break;
                case 2:
                    s.pop();
                    break;
                case 3:
                    s.display();
                    break;
                case 4:
                    System.out.print("Enter the element to search: ");
                    int elem = in.nextInt();
                    s.search(elem);
                    break;
                default:
                    System.out.println("Invalid choice");
            }

            System.out.println("\nEnter 0 to go back to main menu");
            System.out.println("Enter any other number to exit");
            cont = in.nextInt();

        } while (cont == 0);

        System.out.println("Exit Successfully");
        in.close();
    }
}
