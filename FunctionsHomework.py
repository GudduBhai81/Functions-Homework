# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to multiply a list of numbers by a given multiplier
def multiply_list(numbers, multiplier):
    result = []
    for number in numbers:
        result.append(multiply(number, multiplier))
    return result

# Example usage
num1 = 5
num2 = 3
result_single = multiply(num1, num2)
print(f"The result of multiplying {num1} and {num2} is: {result_single}")

# Using a list of numbers with a multiplier
numbers = [1, 2, 3, 4, 5]
multiplier = 4
result_list = multiply_list(numbers, multiplier)
print(f"The result of multiplying the list {numbers} by {multiplier} is: {result_list}")