# Implement stack using linked list
# functions:
#     - push
#     - pop
#     - top
#     - empty

class node(object):

    def __init__(self,data=None,new_next=None):
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

class stack(object):

    def __init__(self,head=None):
        self.head = head

    def push(self,key_value):
        '''
        push element in stack
        '''
        temp = node()
        temp.data = key_value

        if self.head == None:
            self.head = temp 
        else:
            temp.set_next(self.head)
            self.head = temp

    def pop(self):
        '''
        pop element from stack 
        '''
        if self.head == None:
            print('Empty Stack!!')
            return -1

        temp = self.head
        self.head = temp.get_next()

    def print(self):
        '''
        print stack 
        '''
        temp = self.head 

        while(temp):
            print(temp.data,end=' ')
            temp = temp.get_next()

    def isempty(self):
        '''
        check for empty stack
        '''
        if self.head == None:
            print(True)
        else:
            print(False) 

    def top(self):
        '''
        return top element 
        '''
        print(self.head.data) 


##########################################################################################
##########################################################################################

user_stack = stack()

user_stack.push(2)
user_stack.push(4)
user_stack.push(6)
user_stack.push(8)
user_stack.push(10)
user_stack.push(12)
user_stack.push(14)
user_stack.push(16)

user_stack.print()

user_stack.pop()

print('\n')
user_stack.print()

user_stack.pop()

print('\n')
user_stack.print()

print('\n')
user_stack.isempty()
print('\n')
user_stack.top()