temp = int(input('Temparature: '))
is_hot = temp > 65
is_cold = temp < 25


if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it is a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")


jina = input('Name: ')
count = (len(jina))

is_long = (len(jina)) > 50
is_short = (len(jina)) < 3

if is_short:
    print("Name must be at least three characters")
elif is_long:
    print("The name can only be a maximum of 50 characters")
else:
    print("Name looks good!")






