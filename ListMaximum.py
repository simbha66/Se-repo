def find_largest_number(numbers):
    if not numbers:
        return None  # handle empty list case

    largest = numbers[0]  # assume first number is largest
    for num in numbers:
        if num > largest:
            largest = num  # update largest if current number is bigger
    return largest

# Example usage
numbers_list = [12, 45, 78, 23, 90, 34]
result = find_largest_number(numbers_list)
print(f"The largest number is: {result}")
