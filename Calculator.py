class Calculator:
    @staticmethod
    def apply_operator(operators, values, operator):
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

    @staticmethod
    def greater_precedence(op1, op2):
        precedences = {'+': 1, '-': 1, '/': 2, '*': 2}
        return precedences[op1] > precedences[op2]

    def calculate(self, expression):
        operators = []
        values = []
        expression = expression.replace(" ", "")
        i = 0
        while i < len(expression):
            if expression[i] in '0123456789':
                j = i
                while j < len(expression) and expression[j] in '0123456789':
                    j += 1
                values.append(int(expression[i:j]))
                i = j
            else:
                while operators and Calculator.greater_precedence(operators[-1], expression[i]):
                    Calculator.apply_operator(operators, values, operators.pop())
                operators.append(expression[i])
                i += 1

        while operators:
            Calculator.apply_operator(operators, values, operators.pop())
        return values[0]


expression = " 3 * 4 - 2"
result = Calculator().calculate(expression)
print(result)
