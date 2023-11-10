from array import array

searchable = array('i', [8,6,7,4,1,22])
search = int(input("Enter a random number to search in our array: "))

for element in searchable:
    if search==element:
        print(f"{search} is in the array")
        break

else:
    print(f"{search} is not found in the array")
