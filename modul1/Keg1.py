def minus(x, y):
    return x - y

def plus(x, y):
    return x+y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator =='+':
            return plus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))

expression_tree = ('*',('+',2,3),('-',5,1))
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:",result)