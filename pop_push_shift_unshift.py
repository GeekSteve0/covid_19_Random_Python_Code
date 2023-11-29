# pop()

numbers = [1, 2, 3, 4, 5]

last_number = numbers.pop()
print(last_number)   # Output: 5
print(numbers)       # Output: [1, 2, 3, 4]

# push()

numbers.push(6)
print(numbers)       # Output: [1, 2, 3, 4, 6]

# shift()

first_number = numbers.shift()
print(first_number)  # Output: 1
print(numbers)       # Output: [2, 3, 4, 6]

# unshift()

numbers.unshift(0)
print(numbers)       # Output: [0, 2, 3, 4, 6]
