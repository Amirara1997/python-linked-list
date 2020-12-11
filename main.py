class Node :
    def __init__(self, data=None):
        self.data = data
        self.next = None 



class linkedList :
    def __init__(self):
        self.head = Node()

    # def insert_first(self,new_data):
    #     new_node = Node(new_data)
    # new_node.next = self.head
    # self.head = new_node

    # def insert_last (self, new_data):
    #     new_node = Node(new_data)

    #     if self.head is None :
    #         self.head = new_node
    #         return

    #     temp = self.head
    #     while(temp.next):
    #         temp = temp.next     


    # def insert_center (self, prev_node , new_data):
    #     if prev_node is None :
    #         print("your Node must be a node at the linkedlist")
    #         return
    #     new_node = Node(new_data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node

    # def traverse (self):

    #     temp = self.head
    #     while(temp.next):
    #         print(temp.next)
    #         temp = temp.next


    def append(self,new_data) : 
        new_node = Node(new_data)
        temp = self.head
        while temp.next != None :
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
            elems.append(temp_node.data)  
            print elems


    def get(self,index):
        if index>= self.lenght():
            print "ERROR : 'get' index out of range!"
            return None

        temp_idx=0
        temp_node = self.head

        while True :
            temp_node = temp_node.next
            if temp_idx == index:
                return temp_node.new_data
                temp_idx+=1

    def erase (self,index):
        if index >= self.lenght():
            print "ERROR: 'Erase' Index out of range ! "
            return

            temp_idx=0 
            temp_node = self.head
            while True :
                last_node = temp_node
                temp_node = temp_node.next
                if temp_idx ==index :
                    last_node.next = temp_node.next
                    return
                temp_idx+=1    


studencode = input("input studens code : ")

my_list = linkedList()
my_list.append(studencode)
my_list.display()
studencode2 = input("input studens code : ")
my_list.append(studencode2)
my_list.display()
studencode3 = input("input studens code : ")
my_list.append(studencode3)
my_list.display()
my_list.erase(studencode2)
my_list.display()







