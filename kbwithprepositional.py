combinations = [(True,True,True),(True,True,False),(True,False,False),(False,False,False),(False,False,True),(False,True,True)]
variables = {'p':0,'q':1,'r':2}
priority = {"~": 3, "v": 1, "^": 2}
def main() :
    kb = input("Enter the rule : ")
    q = input("Enter the query : ")
    if entailment(kb,q) :
        print("Rule entails the query")
    else :
        print("Rule does not entail the query")

def entailment(kb,q) :
    print("Truth Table : ")
    print("Rule  Query")
    for comb in combinations :
        rule = evaluatePostfix(toPostfix(kb),comb)
        query = evaluatePostfix(toPostfix(q),comb)
        print(rule,query)
        if rule and not query :
            return False
    return True

def toPostfix(infix) :
    stack = []
    postfix = ""
    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParanthesis(c):
                stack.append(c)
            elif isRightParanthesis(c):
                operator = stack.pop()
                while not isLeftParanthesis(operator):
                    postfix += operator
                    operator = stack.pop()
            else:
                while (not isEmpty(stack)) and hasLessOrEqualPriority(c, peek(stack)):
                    postfix += stack.pop()
                stack.append(c)
    while not isEmpty(stack):
        postfix += stack.pop()

    return postfix

def evaluatePostfix(exp,comb) :
    stack=[]
    for i in exp:
        if isOperand(i):
            stack.append(comb[variables[i]])
        elif i == "~":
            val1 = stack.pop()
            stack.append(not val1)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(_eval(i, val2, val1))
    return stack.pop()
    
def _eval(i, val2, val1):
    if i == "^":
        return val2 and val1
    return val2 or val1

def isLeftParanthesis(c):
    return c == "("


def isRightParanthesis(c):
    return c == ")"


def isEmpty(stack):
    return len(stack) == 0


def peek(stack):
    return stack[-1]


def hasLessOrEqualPriority(c1, c2):
    try:
        return priority[c1] <= priority[c2]
    except KeyError:
        return False
    
def isOperand(c):
    return c.isalpha() and c != "v"
    
main()
