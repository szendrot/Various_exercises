def is_number(symbol):
    try:
        int(symbol)
        return True
    except ValueError:
        return False

def eval_postfix(postfix):
    stack = []
    postfix = postfix.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ').split()
    for i in postfix:
        if i.strip() == '':
            continue 
        elif i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "-":
            op2 = stack.pop() 
            stack.append(stack.pop() - op2)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            op2 = stack.pop()
            if op2 != 0.0:
                stack.append(stack.pop() / op2)
            else:
                raise ValueError("division by zero is not allowed!")
        elif is_number(i):
                stack.append(int(i))
        else:
            raise ValueError("unknown char {0}".format(i))
    return stack.pop()
print(eval_postfix('9 3 - 5 * 45 -'))
