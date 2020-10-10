food = [(' '),('Pizza Slice', 4),('Chips' ,1), ('Chicken Tenders' ,5), ('Apple Slices' ,1), ('Turkey Sandwich' ,3),('Pasta' ,8),('Trail Mix' ,2),('Cookies' ,2),('Candy' ,2)]

drinks = [(' '),('Water', 0),('Pepsi', 1), ('Sprite', 1)('Lemonade', 1),('Iced Tea', 1)('Orange Juice', 1)('Wine(Glass)', 4)]

cart_items = 0
item_price1 = drinks[1]
item_price2 = food[1]


def menu():
  while True:
    print("Flight Menu" + "\n"
    "\t(O) Order\n"
    "\t(S) Services\n"
    "\t(P) Payment\n"
    "\t(H) Help\n"
    "\t(E) Exit Menu\n")
    user_input = str(input('How can we help you today?'))      
    if (len(user_input == 1)):
      if(user_input == "O"): #Order Menu
        print("\n")
        def order():
      #elif(user_input == "S"):#Services #expected indented block error, no solution yet
          print("\n")
        def service():
          break
      elif(user_input == "P"): #Payment
        print("\n")
        def payment():
          break
      elif(user_input == "H"): #Help
        print("A flight attendant will be at your assistance shortly.")
        break
      elif(user_input == "E"):
        print("Thank You! Enjoy your Flight.")
      else:
        print(str(user_input) + 'is an Invalid Input. Please Try Again.')
    else:
      print(str(user_input) + 'is an Invalid Input. Please Try Again.')


def order():
  while True:
    print('Order Food/Drinks' "\n"
    '\t(F) Food\n'
    '\t(D) Drinks\n'
    '\t(R) Return to Main Menu')

    user_input = str(input('Select an Option.')).upper #.upper method forces characters to be uppercase
    if (len(user_input == 1)): #If the length of users input is 1 character continue
      if (user_input == "F"):
        print("\n")
        def Food_list():
      elif(user_input == "D"):
        print("\n")
        def Drink_list():
      elif(user_input == "R"):
        def menu():
      else:
        print('Error ' + str(user_input) + ' is an invalid input. Please try again.')
    else:
      print('Error ' + str(user_input) + ' is an invalid input. Please try again.')

def Food_list():
  while True:
    print('Order Food' '\n'
    '\t (D) Drinks\n'
    '\t (P) Payment\n'
    '\t (R) Return to Main Menu\n')
    food.order[0])
    n = int(user_input('What would you like to eat?'))
    if (n == food[0]):
      print(food[1]) #prints item from list in index 0
      cart_items1 += food[n][0]
    elif (str(user_input == 'D'))
        print('\n')
        def Drink_list():
    elif(str(user_input == 'P'))
        print('\n')
        def payment():
    elif (str(user_input == 'R'))
        def menu():
    else:
        print('Error ' + user_input + ' is an invalid input. Please try again.')

def Drink_list():
    while True:
        print('Order Drinks' '\n'
        '\t (F) Food\n'
        '\t (P) Payment\n'
        '\t (R) Return to Main Menu\n'
        drinks[0])
        n = int(user_input('What would you like to drink?'))
        if (n == drinks[0]):
            print(drinks[1])
            cart_items2 += drinks[n][0]
        elif (str(user_input == 'F'))
            print('\n')
            def Food_list():
        elif(str(user_input == 'P'))
            print('\n')
            def payment():
        elif (str(user_input == 'R'))
            def menu():
        else:
            print('Error ' + user_input + ' is an invalid input. Please try again.')

def services():
  while True:
    print('Flight Services' "\n"
    '\t (I) Information\n')
    '\t (R) Return to Main Menu)'
    
    user_input = str(input('Select an Option.')).upper
    if(len(user_input == 1)):
      if (user_input == "I"):
        print("\n")
        def information() #haven't made this module yet
      elif (user_input == "R"):
        def menu()
      else:
        print('Error ' + str(user_input) + ' is an invalid input. Please try again.')
    else:
      print('Error ' + str(user_input) + ' is an invalid input. Please try again.')

def payment(): #Unfinished
    while True:
        print('Payment' '\n')
        total_checkout_price = 0