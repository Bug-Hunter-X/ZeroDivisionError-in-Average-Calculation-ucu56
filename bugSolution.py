def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return total / count

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}") # Output: Average: 0

# Example usage with a list of numbers
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"Average: {average}") # Output: Average: 30.0