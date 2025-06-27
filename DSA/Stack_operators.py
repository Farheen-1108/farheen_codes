operators = set(['+','-','*','/','(',')','^']) 
PRIORITY = {'+':1,'-':1,'*':2,'/':2,'^':3}

def infix_to_postfix(expression):
    stack=[]
    output=''
    for ch in expression:                           #if an apperand then put it directly in postfix
        if ch not in operators:
            output+=ch 
        elif ch=="(":                                # else operators should be in stack
            stack.append('(')
        elif  ch==')':
            while stack and stack[-1]!= '(':           # push cheyali
                output+=stack.pop()
            stack.pop()                                  #pop
        else:                                          # lesser priority can't be on top  on higher or and priority
            #so pop and put in output
            while stack and stack[-1]!='(' and PRIORITY[ch] <=PRIORITY[stack[-1]]:      #stack[-1] means top most
                output+=stack.pop() 

            stack.append(ch)

    while stack:
        output+=stack.pop()

    return output                    
expression = input("enter infix expression")
print("infix expression: ",expression)
print("postfix expression: ",infix_to_postfix(expression))      



      