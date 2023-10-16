# Demonstrates the concept of reversing a Singly Linked Lists, and practicing 
# the use of functions
# Marc Glass
# 10/16/2023




# Node class
class Node:
    #initializing the node object
    def __init__(self, data):
        self.data = data  # assigns data
        self.next = None  # initiating next as null



# Linked list class that contains a Node object
class LinkedList:

    # function to initialize the linked list object
    def __init__(self):
        self.head = None

    # function that reverses the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    

    #inserting new node at beginning of linked list
    def push(self, new_data):

        # allocate the node and put in the data
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node

    def deleteNode(self, pos):
        temp = self.head
        prev = self.head
        for i in range(0, pos):
            if i == 0 and pos == 1:
                self.head = self.head.next

            else:
                if i == pos-1 and temp is not None:
                    prev.next = temp.next
                else:
                    prev = temp
                    if prev is None:
                        break
                    temp = temp.next
                    

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next 

# This function iterates through a given amount of numbers and adds them
# to the linked list. Why? no clue. just wanted to add my own zest. 
def addNumbers(llist):
    y = llist
    for x in range(0, 21, 1):
        y.push(x)
        

def printMessage(llist):
    y = llist
    print("Given linked list:")
    y.printList()
    y.reverse()
    print("\nReversed linked list:")
    y.printList()
    print("\nNow with postive numbers deleted:")
    for x in range(21, 0, -2): 
        y.deleteNode(x)
    
    y.printList()
        


# Driver
def main():
    llist = LinkedList()

    addNumbers(llist)      
    printMessage(llist)
    

if __name__ == "__main__":
    main()
        
        


