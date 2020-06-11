'''
PROBLEM STATEMENT:
Our frient Monk has been made teacher for the day today by his school professor. He is going to teach 
informatics to his colleagues as that is his favorite subject. Before entering the class, Monk realized that he 
does not remember the names of all his collegaues clearly. He thinks this will cause problems and will
not allow him to teach the class well. However, Monk remembers the roll number of all his colleagues very
well.Monk now wants you to help him out. He will initially give you a list indicating the name and roll number of 
of all  his colleagues. When he enters the class he will give yoiu the roll number of any of his colleagues
belonging to the class. You need to revert to him with the name of that colleague.

INPUT FORMAT:
The first line contains a single intergers N denoting the number of Monk's colleagues. Each of the next N
lines contains an integer and a string denoting the roll number and name of the ith collegue of Monk.
THe next line contains a single integer q denoting the number of queries Monk shall present to you when he starts
teaching in class. Each of the next q lines contains a single integer x denoting the oll number of the 
student whose name Monk wants to know.

OUTPUT FORMAT:
You need to print q strings, each string on a new link, indicating the answers to each of Monk's queries.

NOTE:
The name of each student shall consist of lowercsae English alphabets only. It is guaranteed that the roll number
appearing in each query shall belongs to some student from the class.

SAMPLE INPUT:
5
1 akshay
2 test
3 marcus
4 rama
5 vishal
2
1
2

SAMPLE OUTPUT:
akshay
test

'''

class node(object):

    def __init__(self,new_data=None,new_next=None,new_name=None):
        self.data = new_data
        self.next = new_next
        self.name = new_name

    def getData(self):
        return self.data 

    def setData(self,new_data):
        self.data = new_data

    def getNext(self):
        return self.next

    def setNext(self,new_next):
        self.next = new_next

    def getName(self):
        return self.name 

    def setName(self,new_name):
        self.name = new_name


class linkedList(object):

    def __init__(self,new_head=None):
        self.head = new_head

    def insertNode(self,new_data,new_name):
        '''
        Insert node in the linked list 
        Arg: 
             new_data - roll number to insert 
             new_name - student name 
        '''

        temp = node()
        temp.setData(new_data)
        temp.setName(new_name)
        temp.setNext(self.head)
        self.head = temp 

    def searchNode(self,new_data):
        '''
        search node with roll number new_data
        Arg: 
             new_data: roll number to be searched
        '''

        temp = self.head 
        while(temp):
            if temp.getData() == new_data:
                ls_name = temp.getName()
                return ls_name 
            temp = temp.getNext()
        return 'NOT FOUND'

    def print(self):
        '''
        print the linked list 
        '''
        temp = self.head 
        while(temp):
            print(str(temp.getData())+','+temp.getName(),end=' --> ')
            temp = temp.getNext()


class hash(object):

    def __init__(self,size=5):
        self.students = [None] * size
        self.arraylength = size 

    def hashFunc(self,roll_num):
        '''
        return hashed key
        Arg:
             roll_num - hashed key
        '''
        return roll_num % self.arraylength

    def insertStudent(self,roll_num,name):
        '''
        Insert student entry into hash table
        Arg: 
             roll_num - roll number for student
             name - name of the student
        '''

        ll_index = self.hashFunc(roll_num)

        if (self.students[ll_index] == None):
            student_linkedlist = linkedList()
        else:
            student_linkedlist = self.students[ll_index]

        student_linkedlist.insertNode(roll_num,name)
        self.students[ll_index] =  student_linkedlist

    def search(self,roll_num):
        '''
        search the entry into the hash table
        Arg:
             roll_num - roll number for which name has to be retrieved.
        '''

        ll_index = self.hashFunc(roll_num)
        ll_user_link = self.students[ll_index]
        if ll_user_link != None:
            return ll_user_link.searchNode(roll_num)

    def printHash(self):
        '''
        print hash table
        '''

        ll_length = self.arraylength - 1
        while(ll_length >= 0):
            if self.students[ll_length]:
                ll_item = self.students[ll_length]
                if ll_item != None:
                    print(ll_item.print())
            ll_length = ll_length - 1 


print('-----------------------------------------------------------------')

user_hash = hash()

while(1):
    entries = input('No of Entries?? ')
    if not entries.isnumeric():
        print('INVALID ENTRY... TRY AGAIN')
        continue 
    entries = int(entries)
    break 

print('-----------------------------------------------------------------')
print('Enter Values:        ROLL NUMBER     NAME')
print('-----------------------------------------------------------------')

while(entries):
    ls_input = input()
    if ls_input.find(' ') == -1:
        print('INVALID ENTRY... TRY AGAIN')
        continue 

    ls_roll_no, ls_name = ls_input.split(' ')

    if ls_roll_no == '' or ls_name == '' or ( not ls_roll_no.isnumeric() ):
        print('INVALID ENTRY... TRY AGAIN')
        continue

    ll_roll_no = int(ls_roll_no)

    user_hash.insertStudent(ll_roll_no,ls_name)
    entries = entries - 1

print('-----------------------------------------------------------------')
user_hash.printHash()
print('-----------------------------------------------------------------')

ls_user_req = input('Type Roll No to search [ X to close ]: ')

while(ls_user_req.upper() != 'X'):
    if ( ls_user_req.upper() != 'X'):
        if not ls_user_req.isnumeric():
            print('INVALID ENTRY... TRY AGAIN')
        else:
            print(user_hash.search(int(ls_user_req)))
    else:
        break 
    ls_user_req = input('Type Roll No to search [ X to close ]: ')