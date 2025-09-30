def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2!= 0:
                return num1/num2
            elif num2 == 0:
                return "Error: Division by zero is impossible."
            
                
        case _:
            return "Error: Invalid operation. Please choose add, subtract, multiply, or divide."




        

