# Implement stack using linked list
# functions:
#     - push
#     - pop
#     - top
#     - empty

class node(object):

    def node(self,data=None,new_next=None):
        self.data = data 
        self.next = new_next

    def get_data(self):
        '''
        get node data 
        '''
        return self.data 

    def get_next(self):
        '''
        get next node 
        '''
        return self.next 

    def set_next(self,new_next):
        '''
        set next node
        '''
        self.next = new_next 

class linkedlist(object):

    def linkedlist(self,head=None):
        self.head = None

    def insert(self,key_value):
        '''
        insert element in link list
        '''
        temp = node()
        temp.data = key_value

        if self.head == None:
            self.head = temp 
        else:
            temp.set_next(self.head)
            self.head = temp

    def delete(self):
        '''
        delete element from link list 
        '''
        if self.head == None:
            return -1

        temp = self.head
        self.head = temp.get_next()

    def print(self):
        '''
        print link list 
        '''
        temp = self.head 

        while(temp):
            print(temp.data)
            temp = temp.get_next()


##########################################################################################
##########################################################################################

user_linklist = linkedlist()

user_linklist.insert(2)
user_linklist.insert(4)
user_linklist.insert(6)

user_linklist.print()

user_linklist.remove()

print('\n')
user_linklist.print()