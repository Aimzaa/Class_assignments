# 🔹 Problem 1: Reverse a String
# Write a function that takes a string as input and returns the reversed string.
# Example:
# 🔹 Input: "hello"
# 🔹 Output: "olleh"
# 💡 Hint: Use Python's slicing feature.

def reverse_strings(s):
    return s[::-1]

print(reverse_strings("hello"))
print(reverse_strings("world"))





# 🔹 Problem 2: Count Vowels in a String
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
# Example:
# 🔹 Input: "Apple"
# 🔹 Output: 2
# 💡 Hint: Use a loop and check if each character is in a set of vowels.

def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0

# Convert string to lowercase for case-insensitive comparison
    lower_string = input_string.lower()

    for char in lower_string:
        if char in vowels:
            count += 1

    return count

# Test the function
if __name__ == "__main__":
    test_string = 'Apple'
    print(f"Input: '{test_string}'")
    print(f"Output: {count_vowels(test_string)}")



# 🔹 Problem 3: Sum of Digits
# Write a function that takes a non-negative integer and returns the sum of its digits.
# Example:
# 🔹 Input: 1234
# 🔹 Output: 10
# 💡 Hint: Convert the number to a string and iterate over each digit or use modulus and division.

def sum_of_digits(number):

# We will convert the number to a string and then convert each digit back to an integer    
    return sum(int(digit) for digit in str(number))

# Test the function
if __name__ == "__main__":
    print(sum_of_digits(1234))
    print(sum_of_digits(999))
    print(sum_of_digits(1996))
