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