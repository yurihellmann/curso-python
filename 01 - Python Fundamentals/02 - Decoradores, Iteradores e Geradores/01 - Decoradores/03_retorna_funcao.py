def calculadora(operacao):
    def soma(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    def multi(a,b):
        return a*b
    
    def divi(a,b):
        return a/b
    
    match operacao:
        case '+':
            return soma
        case '-':
            return sub
        case '*':
            return multi
        case '/':
            return divi
        
op = calculadora("+")
print(op(2,2))
op = calculadora("-")
print(op(2,2))
op = calculadora("*")
print(op(2,2))
op = calculadora("/")
print(op(2,2))