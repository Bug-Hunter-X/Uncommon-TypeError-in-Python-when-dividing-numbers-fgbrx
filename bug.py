def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            raise TypeError("Type error but both are numbers")
        else:
            print("Error: Type mismatch")
            return None

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: Error: Type mismatch
print(function_with_uncommon_error("hello",10)) # Output: Error: Type mismatch
print(function_with_uncommon_error(10.5,3)) # Output: 3.5