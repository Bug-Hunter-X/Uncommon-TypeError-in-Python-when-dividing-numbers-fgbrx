def function_with_uncommon_error_solution(a, b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise TypeError("Operands must be numbers")
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

# Example usage
print(function_with_uncommon_error_solution(10, 2))  # Output: 5.0
print(function_with_uncommon_error_solution(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error_solution(10, "hello")) # Output: TypeError: Operands must be numbers
print(function_with_uncommon_error_solution("hello",10)) # Output: TypeError: Operands must be numbers
print(function_with_uncommon_error_solution(10.5,3)) # Output: 3.5