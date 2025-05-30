import java.util.Scanner;

class CircularQueue {
    int[] queue = new int[10];  // Fixed-size array
    int front = -1;
    int rear = -1;
    int size = 0;

    // 1. isEmpty
    boolean isEmpty() {
        return size == 0;
    }

    // 2. isFull
    boolean isFull() {
        return size == queue.length;
    }

    // 3. Enqueue
    void enqueue(int value) {
        if (isFull()) {
            System.out.println("Queue is full (Overflow)");
            return;
        }

        if (isEmpty()) {
            front = 0;
        }

        rear = (rear + 1) % queue.length;
        queue[rear] = value;
        size++;
        System.out.println("Element " + value + " enqueued.");
    }

    // 4. Dequeue
    void dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty (Underflow)");
            return;
        }

        int removed = queue[front];
        front = (front + 1) % queue.length;
        size--;

        if (size == 0) {
            front = rear = -1;
        }

        System.out.println("Element " + removed + " dequeued.");
    }

    // 5. Peek
    void peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
        } else {
            System.out.println("Front element: " + queue[front]);
        }
    }

    // 6. Size
    int currentSize() {
        return size;
    }

    // 7. Display
    void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return;
        }

        System.out.print("Queue elements: ");
        for (int i = 0; i < size; i++) {
            int index = (front + i) % queue.length;
            System.out.print(queue[index] + " ");
        }
        System.out.println();
    }
}

public class CircularQueueArray {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        CircularQueue cq = new CircularQueue();
        int choice;

        do {ss
            System.out.println("\n=== Circular Queue Menu ===");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek (front element)");
            System.out.println("4. Check if queue is empty");
            System.out.println("5. Check if queue is full");
            System.out.println("6. Current size");
            System.out.println("7. Display queue");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            choice = in.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter element to enqueue: ");
                    int item = in.nextInt();
                    cq.enqueue(item);
                    break;
                case 2:
                    cq.dequeue();
                    break;
                case 3:
                    cq.peek();
                    break;
                case 4:
                    System.out.println("Queue is " + (cq.isEmpty() ? "empty" : "not empty"));
                    break;
                case 5:
                    System.out.println("Queue is " + (cq.isFull() ? "full" : "not full"));
                    break;
                case 6:
                    System.out.println("Current size: " + cq.currentSize());
                    break;
                case 7:
                    cq.display();
                    break;
                case 0:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }

        } while (choice != 0);

        in.close();
    }
}

