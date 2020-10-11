# @authors: 
# Burak Turksever
# Mehmet Yaylaci
# Eralp Kumbasar
import ui

choice = str(input("Would you like to run the program with the default data? (yes/no)"))
if choice.upper() == 'YES':
  solver = ui.Graph()
  print("3 Cannibals 3 Missionaries and a Boat of Capacity 2")
  solver.DFS_start(3, 2)
  # Question 1 answer
  print("5 Cannibals 5 Missionaries and a Boat of Capacity 3")
  solver.DFS_start(5, 3)
  # Question 2a answer
  print("6 Cannibals 6 Missionaries and a Boat of Capacity 4")
  # Question 2b answer 
  solver.DFS_start(6, 4)
  print("6 Cannibals 6 Missionaries and a Boat of Capacity 5")
  solver.DFS_start(6, 5)
  solver.draw_graph()
elif choice.upper() == 'NO':
  while True:
    input_one = str(input('\nPlease enter the number of Missionaries and Cannibals (EXIT to exit): '))
    if input_one.upper() == 'EXIT':
      break
    else:
      if input_one.isnumeric() and int(input_one) <= 494:
        number = int(input_one)
        input_two = str(input('Please enter the capacity of the boat: '))
        if input_two.isnumeric():
          capacity = int(input_two)
          if (capacity >= 2 and number <= 3) or ((number == 4 or number == 5) and capacity == 3) or (capacity >= 4 and number >= 6):
            solver = ui.Graph() 
            solver.DFS_start(number, capacity)
            solver.draw_graph()
          else:
            print('\nThis combination will not work! See why on https://arxiv.org/pdf/1802.09369.pdf\n')
        else:
          print('Please enter a valid number.')  
      elif input_one.isnumeric() and int(input_one)>494:
        print("The entered number is too large (recursion limit of Python is reached when executed.)")
      else:
        print('Please enter a valid number.')
else:
  print('Unrecognized input')