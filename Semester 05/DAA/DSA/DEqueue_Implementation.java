import java.util.Scanner;

class DEQueue {
    int size = 10;
    int[] queue = new int[size];
    int front = -1;
    int rear = -1;

    boolean isEmpty() {
        return front == -1;
    }

    boolean isFull() {
        return (front == 0 && rear == size - 1) || (front == rear + 1);
    }

    void enqueueFront(int item) {
        if (isFull()) {
            System.out.println("Queue is Full (Overflow)");
            return;
        }

        if (isEmpty()) {
            front = rear = 0;
        } else if (front == 0) {
            front = size - 1;
        } else {
            front--;
        }

        queue[front] = item;
        System.out.println("Item inserted at front.");
    }

    void enqueueRear(int item) {
        if (isFull()) {
            System.out.println("Queue is Full (Overflow)");
            return;
        }

        if (isEmpty()) {
            front = rear = 0;
        } else if (rear == size - 1) {
            rear = 0;
        } else {
            rear++;
        }

        queue[rear] = item;
        System.out.println("Item inserted at rear.");
    }

    void dequeueFront() {
        if (isEmpty()) {
            System.out.println("Queue is Empty (Underflow)");
            return;
        }

        System.out.println("Item removed from front: " + queue[front]);

        if (front == rear) {
            front = rear = -1;
        } else if (front == size - 1) {
            front = 0;
        } else {
            front++;
        }
    }

    void dequeueRear() {
        if (isEmpty()) {
            System.out.println("Queue is Empty (Underflow)");
            return;
        }

        System.out.println("Item removed from rear: " + queue[rear]);

        if (front == rear) {
            front = rear = -1;
        } else if (rear == 0) {
            rear = size - 1;
        } else {
            rear--;
        }
    }

    void display() {
        if (isEmpty()) {
            System.out.println("Queue is Empty");
            return;
        }

        System.out.print("Queue elements: ");
        int i = front;
        while (true) {
            System.out.print(queue[i] + " ");
            if (i == rear) break;
            i = (i + 1) % size;
        }ss
        System.out.println();
    }
}

public class DEqueue_Implementation {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        DEQueue dq = new DEQueue();
        int choice;

        do {
            System.out.println("\n=== DEQueue Operations Menu ===");
            System.out.println("1. Check if queue is empty");
            System.out.println("2. Check if queue is full");
            System.out.println("3. Enqueue at front");
            System.out.println("4. Enqueue at rear");
            System.out.println("5. Dequeue from front");
            System.out.println("6. Dequeue from rear");
            System.out.println("7. Display queue");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            choice = in.nextInt();

            switch (choice) {
                case 1:
                    System.out.println("Queue is " + (dq.isEmpty() ? "empty" : "not empty"));
                    break;
                case 2:
                    System.out.println("Queue is " + (dq.isFull() ? "full" : "not full"));
                    break;
                case 3:
                    System.out.print("Enter element to insert at front: ");
                    dq.enqueueFront(in.nextInt());
                    break;
                case 4:
                    System.out.print("Enter element to insert at rear: ");
                    dq.enqueueRear(in.nextInt());
                    break;
                case 5:
                    dq.dequeueFront();
                    break;
                case 6:
                    dq.dequeueRear();
                    break;
                case 7:
                    dq.display();
                    break;
                case 0:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice, please try again.");
            }

        } while (choice != 0);

        in.close();
    }
}
