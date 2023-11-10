# for loop
prices = [10, 20, 30]

total = 0
for price in prices:
    total = total + price
print(f"The total price is {total}")

names = ['Gachiri', 'Wambui', 'Phyllis', 'Abel', 'Steve']
for index, ournames in enumerate(names):
        print(index, ournames)

for item in range(10, 100, 2):
    print(item)

# Nested loops
for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')

numbers = [1, 1, 1, 1, 6]
for x_count in numbers:
    output = ''
#    for count in range(x_count):
#        output += 'x'
#        print(output)
#        print('x' * x_count)

#Lists
hiphop = ['Dior', 'backseat', 'intentions', 'woo', 'quavo', 'migos', 'pop smoke', 'offset', 'breezy']
print(hiphop[3:7])

marks = [100, 900, 7586, 894, 758, 499, 443, 80, 23, 22, 9]
max = marks[0]
for number in marks:
    if number > max:
        max = number
print(max)


# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0] [1])
# using nested loop to iterate over the whole matrix
for row in matrix:
    for item in row:
        print(item)

# List methods
numbers = [5, 2, 1, 7, 32]
numbers.insert(4, 90)
print(numbers)
numbers.remove(5)
print(numbers)
#numbers.clear()
#print(numbers)
numbers.pop()
print(numbers)
number.sort()
print(numbers)


# Python 3 program for Bresenham’s Line Generation
# Assumptions :
# 1) Line is drawn from left to right.
# 2) x1 < x2 and y1 < y2
# 3) Slope of the line is between 0 and 1.
# We draw a line from lower left to upper
# right.


# function for line generation
def bresenham(x1,y1,x2, y2):

    m_new = 2 * (y2 - y1)
    slope_error_new = m_new - (x2 - x1)

    y=y1
    for x in range(x1,x2+1):

        print("(",x ,",",y ,")\n")

        # Add slope to increment angle formed
        slope_error_new =slope_error_new + m_new

        # Slope error reached limit, time to
        # increment y and update slope error.
        if (slope_error_new >= 0):
            y=y+1
            slope_error_new =slope_error_new - 2 * (x2 - x1)




# driver function
if __name__=='__main__':
    x1 = 3
    y1 = 2
    x2 = 15
    y2 = 5
    bresenham(x1, y1, x2, y2)

#This code is contributed by ash264

