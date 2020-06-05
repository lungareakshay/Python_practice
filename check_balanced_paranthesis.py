# Check Balance Paranthesis using stack

from collections import deque

# paranthesis pairs
ls_start = ['(','[','{']
ls_end = [')',']','}']

#user string
ls_expression = '''
a = (b + c)
d = {(a) * [e + f]}
g = {[(d)]} + (m * n) - [(v)]
'''

def check_balanced():
    '''
    Check for balanced Paranthesis
    Return 1 : Expression is balanced 
    Return -1 : Expression is not balanced
    '''
    user_stack = deque()

    for _ in ls_expression:

        # Insert opening paranthesis
        if _ in ls_start:
            user_stack.append(_)
            
        # Pop paired paranthesis
        if _ in ls_end:
            if user_stack:
                ls_top = user_stack[-1]
               
                if _ == ')' and ls_top == '(':
                    pass 
                elif ( _ == ']' and ls_top == '['):
                    pass 
                elif (_ == '}' and ls_top == '{'):
                    pass 
                else: 
                    return -1
                user_stack.pop()
            else:
                return -1
            
    # Finally check for empty stack
    if user_stack:
        return -1
    else:
        return 1

           
# call function 
if check_balanced() == 1 :
    print('Expression is Balanced')
else:
    print('Expression is not Balanced')