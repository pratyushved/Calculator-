def calculation(expression):
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    def greater_precedence(op1, op2):
        precedences = {'+': 1, '-': 1, '/': 2, '*': 2}
        return precedences[op1] > precedences[op2]

    operators = []
    values = []
    i = 0
    expression = expression.replace(" ", "")
    while i < len(expression):
        if expression[i] in '0123456789':
            j = i
            while j < len(expression) and expression[j] in '0123456789':
                j += 1
            values.append(int(expression[i:j]))
            i = j
        else:
            while operators and greater_precedence(operators[-1], expression[i]):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1

    while operators:
        apply_operator(operators, values)
    return values[0]


expression = " 3 * 4 - 2"
result = calculation(expression)
print(result)