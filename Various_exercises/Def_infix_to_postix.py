operators = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 


def infix_to_postfix(user_input): #input expression
    stack = [] # initially stack empty
    postfix = '' # initially output empty
    for i in user_input:
        if i not in operators:  # if an operand then put it directly in postfix expression
            postfix+= i
        elif i=='(':  # else operators should be put in stack
            stack.append('(')
        elif i==')':
            while stack and stack[-1]!= '(':
                postfix+=stack.pop()
            stack.pop()
        else:
            # lesser priority can't be on top on higher or equal priority    
            # so pop and put in output   
            while stack and stack[-1]!='(' and priority[i]<=priority[stack[-1]]:
                postfix+=stack.pop()
            stack.append(i)
    while stack:
        postfix+=stack.pop()
    return postfix
print(infix_to_postfix('1 * ( 2 +3) * 4'))
