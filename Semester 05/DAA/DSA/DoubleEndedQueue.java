public class DoubleEndedQueue {
    /*
    
    Double Ended Queue() (DEqueue)


    |--------------------|
    |                    |-1 0        1         2         3    <==  index
    |                    |  O         O         O         O
    |       STORE        |  ||        ||        ||        ||
    |                    |  //        //        //        // 
    |                    |  P1        P2        P3        P4
    |--------------------| (FRONT)                      (REAR)
     


Queue FIFO     / (insertion rear deletion first)
DEqueue FIFI   X (insertion      rear + front
                  deletion       rear + front)

 two types of DEqueue
   1 restricted input DEqueue  (cant do insertion from front )                
   2 restricted output DEqueue  (deletion from rear is  not allowed)       
   
   Methods to implement in DEqueues
     1. data (same as queue)
     2. operation 
         1. isEmpty()
         2. isFull()
         3. enequeuefront()
         4. enequeuerear()
         5. dequeuefront()
         6. dequeuerear()
         7. display()


     */
    
}
