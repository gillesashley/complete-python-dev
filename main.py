# Code Snippet 1
def calculate_average(numbers):
    count = len(numbers)
    if count == 0:
        return None
    total = sum(numbers)
    avg = total / count
    return avg


# Test the function
numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("The average is:", result)
