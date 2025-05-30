/* 
Stack 
Def : A stack is collection of elemenet with certain operation called LIFO / FILO disciplane 
A stack can be implemented using array or linklist
stack is a linear data structure 
operation performed in LIFO manner (last in first out) and FILO(first in last out)
mean if we want to remove item the last added item (peak element) remove first and  the last item 
(which is added by firstly is removed in last)

removed in manner
first remove item 3
then remove item 2
and lastly remove item 1

take  a container and add an item from top of container unless it full or requiremenet
let  container


|  item     3  |
|  item     2  |
|  item     1  |
|  container   |
----------------

 container has limit if we cross it limit it (stack) become overflow condition called stackoverflow

 Application of stack
  1. used to call function
  2. parenthesis matching (humen ager parenthesis matching ek expression 
  mn kerni perti hai ager ek mathamatical expression likha hai  jismn parenthesis ka use hua hai to
  kya wo mathamatic expression valid ha ?) and many more..

  Stack ADT (Abstract datatype) 

  in order to create a stack we need a pointer to the topmost (peak) element along with other element 
  which are stored inside 

  operation in Stack ADT are :
    1. push() add an element to stack (btana hoga konsa element)
    2. pop() remove element  (always removed peak element) (btani ki need nahin )
    3. peak operation (check the element index number (oper se neche se nahin))
    4. isEmpty() determine if stack is empty or not
    ager stack khali hai to pop nh ker sakte 
    5. isFull() determine if stack is full or not 
    ager stack full hai to push nh ker sakte 

      

  */