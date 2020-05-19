# Python Commment Utility

This utility to add comment has been created using tkinter.
- It helps user to standardize the comments in projects.
- It helps us to track the changes as it contains Date, Work Item, Programmer Name and Description for which changes has been made.
- When user click on buttons a) Header b) Single Line c) Block, the comment format will be copied on clipboard, user just need to paste wherever it is required.
- Only once user need to add Programmer Name, Work Item Number and Description for defect, then utility will store this value into windows registry and use it for comment, hence this will reduce time for commenting.
- Once user click on any button utility will go in minimize view hence reduce clicks for user.

[EXE Path]:(https://github.com/lungareakshay/Python_practice/blob/master/comment_utility/dist/comment_main.exe)

There are three types of comment this utility provide:

# Header Comment
```
####################################################################
#Function\Module: sum
#                a: first number, b: second number
#Return Arg: total: int
#           
#Description: adds the numbers passed to function
#           
# Date         Work Item        Programmer      Description
# 2020-05-17   WI#77768         AkshayL         return sum of numbers
####################################################################
def sum(a,b):
  return a + b
```
# Single Line Comment
```
# Date:2020-05-17   Work Item: WI#77768       Programmer: AkshayL    Description: Change made for addition
c = a + b
```
# Block comment
```
.
.
# START Date: 2020-05-17   Work Item: WI#77768       Programmer: AkshayL   Description: Changes made for addition
c = a + b
e = c + d
# END Date: 2020-05-17   Work Item: WI#77768       Programmer: AkshayL
.
.
```
