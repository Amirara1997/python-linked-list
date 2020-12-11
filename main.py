class Node :
    def __init__(self, data):
        self.data = data
        self.next = None 



class linkedList :
    def __init__(self):
    self.head = None 


    def insert_first(self,new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

    def insert_last (self, new_data):
        new_node = Node(new_data)

        if self.head is None :
            self.head = new_node
            return

        temp = self.head
        while(temp.next):
            temp = temp.next     


    def insert_center (self, prev_node , new_data):
        if prev_node is None :
            print("your Node must be a node at the linkedlist")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def traverse (self):

        temp = self.head
        while(temp.next):
            print(temp.next)
            temp = temp.next


    def append(self,new_data) : 
        new_node = Node(new_data)
        temp = self.head
        while cur.next != None :
            temp = temp.next 
        temp.next = new_node


    def lenght(self):
        temp = self.head
        total = 0
        while temp.next != None :
            total+=1
            temp = temp.next
        return total


    def display (self):
        elems = []
        temp_node = self.head
        while temp_node.next != None :
            temp_node = temp_node.next
            elems.append(temp_node.new_data)  
            print elems




            







