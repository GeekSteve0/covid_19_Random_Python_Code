#weight = input("Enter your weight: ")
#weight = float(weight)
#unit = input('(L)bs or (K)g: ')
#if unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"You are {converted} kilos.")
#else:
#    converted = weight / 0.45
#    print(f"You are {converted} pounds.")

# WHILE LOOP
#while i <= 10:
 #  print('$' * i )
#i = 1
#   print(i)
 #   if i == 3:
  #      break
   # i += 1

#i = 0
#while i < 6:
 #   i += 1
  #  if i == 3:
   #     continue
    #print(i)
#GUESS GAME
#secret_number = 9
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
 #   guess = int(input('Guess: '))
  #  guess_count += 1
   # if guess == secret_number:
    #    print("You won")
     #   break
#else:
 #       print("You failed")

#CAR ENGINE

command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Truck is already running")
        else:
            started = True
            print("Kenworth started, idling for pressure.")
    elif command == "stop":
        if not started:
            print("Truck is already stopped")
        else:
            started = False
            print("Kenworth stopped, idle for a while before turning off")
    elif command =="quit":
        break
    elif command == "help":
           print(""""
start - starts the truck
stop - stops the truck
quit - exits the program
    
        """)
    else:
        print("Are you high Steve, this truck doesn't fucking understand you ")










#pets = ['cats', 'dogs', 'rabbits', 'hamsters']
#for index, myPets in enumerate(pets):
 #   print(index, myPets)

#steve = ['date', 'time', 'year', 'month']
#for zeejay in steve:
#    print(zeejay)

#i = 5
#while i>0:

 #   i = i *1287905643
 #   print(i)











