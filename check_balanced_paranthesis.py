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

for _ in ls_expression:
    print(_)

user_stack = deque()

user_stack.append('test')

print(user_stack)