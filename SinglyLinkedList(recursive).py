# Demonstrates the concept of Singly Linked Lists
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


    #inserting new node at beginning of linked list
    def push(self, new_data):

        # allocate the node and put in the data
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node


    # counts the number of nodes in linked list
    def getCountRecursive(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRecursive(node.next)

    #wrapper over getCountRecursive()
    def getCount(self):
        return self.getCountRecursive(self.head)



# Driver
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)


    print("Count of nodes is: ", llist.getCount())
    
        
        


