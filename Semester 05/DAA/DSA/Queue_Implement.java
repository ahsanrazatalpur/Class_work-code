import java.util.Scanner;

class Queue {
    int[] queue = new int[10];  // Fixed size array
    int front = -1;
    int rear = -1;

    // 1. Enqueue
    void enqueue(Scanner in) {
        if (isFull()) {
            System.out.println("Queue is Full (Overflow)");
        } else {
            System.out.print("Enter an element to enqueue: ");
            int item = in.nextInt();
            if (front == -1) front = 0; // first element added
            rear++;
            queue[rear] = item;
            System.out.println("Item added to queue.");
        }
    }

    // 2. Dequeue
    void dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is Empty (Underflow)");
        } else {
            System.out.println("Item removed: " + queue[front]);
            if (front == rear) {
                // Only one element was present
                front = -1;
                rear = -1;
            } else {
                front++;
            }
        }
    }

    // 3. Show value at a given index
    void showPeek(int index) {
        if (isEmpty() || index < front || index > rear) {
            System.out.println("Invalid index.");
        } else {
            System.out.println("Element at index " + index + " is: " + queue[index]);
        }
    }

    // 4. Show first value
    void showFront() {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
        } else {
            System.out.println("Front element is: " + queue[front]);
        }
    }

    // 5. Show last value
    void showRear() {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
        } else {
            System.out.println("Rear element is: " + queue[rear]);
        }
    }

    // 6. isEmpty
    boolean isEmpty() {
        return front == -1;
    }

    // 7. isFull
    boolean isFull() {
        return rear == queue.length - 1;
    }

    // Display all queue elements
    void display() {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
        } else {
            System.out.println("Queue Elements:");
            for (int i = front; i <= rear; i++) {
                System.out.print(queue[i] + " ");
            }
            System.out.println();
        }
    }
}

public class Queue_Implement {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Queue q = new Queue();
        int choice;

        do {
            System.out.println("\n=== Queue Operations Menu ===");
            System.out.println("1. Enqueue (Add an element)");
            System.out.println("2. Dequeue (Remove an element)");
            System.out.println("3. Show value at index");
            System.out.println("4. Show first value of the queue");
            System.out.println("5. Show last value of the queue");
            System.out.println("6. Check if queue is empty");
            System.out.println("7. Check if queue is full");
            System.out.println("8. Display all elements");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            choice = in.nextInt();

            switch (choice) {
                case 1:
                    q.enqueue(in);
                    break;
                case 2:
                    q.dequeue();
                    break;
                case 3:
                    System.out.print("Enter index to check: ");
                    int index = in.nextInt();
                    q.showPeek(index);
                    break;
                case 4:
                    q.showFront();
                    break;
                case 5:
                    q.showRear();
                    break;
                case 6:
                    System.out.println("Queue is " + (q.isEmpty() ? "empty" : "not empty"));
                    break;
                case 7:
                    System.out.println("Queue is " + (q.isFull() ? "full" : "not full"));
                    break;
                case 8:
                    q.display();
                    break;
                case 0:
                    System.out.println("Exiting program...");
                    break;
                default:
                    System.out.println("Invalid choice, please try again.");
            }

        } while (choice != 0);

        in.close();
    }
}
