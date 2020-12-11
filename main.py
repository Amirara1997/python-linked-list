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



units = {
    1 : "riazi 1",
    2 : "fizik 1 ",
    3 : "andishe 1",
    4 : "mabani barnameh nevisi",
    5 : "varzeh 1"
}




blist = ["amirreza",9721973128]


# with open('test.txt','r') as file :
#    blist= json.load(file) 



studenlists = linkedList()
studenlists.append(blist)



print("welcome to system \n please choice blews numbers :")
print("1- show student\n2- add studens\n3-selecting a univerciry studens\n4-login\n")
m = input("number ...")
if m == 1 :
    print("show studens page ")
    f = open("test.txt","r")
    print(f.read())
elif m == 2 :
    print("add student")
    n = input("enter studen code:")
    d = str(input("enter studen name...(name must be enterd in '') :"))
    mlist= [n,d]
    studenlists.append(mlist)
    with open ('test.txt','a') as filewrite :
        json.dump(mlist,filewrite)
    print("done")
elif m == 3 :
    print("selecting a univerciry studens")
    print(units)
elif m==4:
    print("enter your studen code \n")
    w = input("code:")
else :
    print("Error : please enter exsted numbers")




