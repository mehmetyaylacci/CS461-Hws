# @authors: 
# Burak Turksever
# Mehmet Yaylaci
# Eralp Kumbasar
import graph

choice = str(input("Would you like to run the program with the default data? (yes/no)"))
if choice.upper() == 'YES':
  solver = graph.Graph()
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
            solver = graph.Graph() 
            solver.DFS_start(number, capacity)
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



'''
-------------------------------------------------------
           OUTPUT THAT ANSWERS THE QUESTIONS
-------------------------------------------------------

5 Cannibals 5 Missionaries and a Boat of Capacity 3 (Question 1)

Depth:1
Current Node: 
Left:(Cannibals: 4 Missionaries: 4)
Right:(Cannibals: 1 Missionaries: 1)
 

Depth:2
Current Node: 
Left:(Cannibals: 4 Missionaries: 5)
Right:(Cannibals: 1 Missionaries: 0)
 

Depth:3
Current Node: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 2 Missionaries: 2)
 

Depth:4
Current Node: 
Left:(Cannibals: 3 Missionaries: 5)
Right:(Cannibals: 2 Missionaries: 0)
 

Depth:5
Current Node: 
Left:(Cannibals: 1 Missionaries: 5)
Right:(Cannibals: 4 Missionaries: 0)
 

Depth:6
Current Node: 
Left:(Cannibals: 2 Missionaries: 5)
Right:(Cannibals: 3 Missionaries: 0)
 

Depth:7
Current Node: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 3 Missionaries: 3)
 

Depth:8
Current Node: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 2 Missionaries: 2)
 

Depth:9
Current Node: 
Left:(Cannibals: 3 Missionaries: 0)
Right:(Cannibals: 2 Missionaries: 5)
 

Depth:10
Current Node: 
Left:(Cannibals: 4 Missionaries: 0)
Right:(Cannibals: 1 Missionaries: 5)
 

Depth:11
Current Node: 
Left:(Cannibals: 2 Missionaries: 0)
Right:(Cannibals: 3 Missionaries: 5)
 

Depth:12
Current Node: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 3 Missionaries: 3)
 

Depth:13
Current Node: 
Left:(Cannibals: 1 Missionaries: 0)
Right:(Cannibals: 4 Missionaries: 5)
 

Depth:14
Current Node: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 4 Missionaries: 4)
 

Depth:15
Current Node: 
Left:(Cannibals: 0 Missionaries: 0)
Right:(Cannibals: 5 Missionaries: 5)

-------------------------------------------------------

6 Cannibals 6 Missionaries and a Boat of Capacity 4 (Question 2a)

Depth:1
Current Node: 
Left:(Cannibals: 5 Missionaries: 5)
Right:(Cannibals: 1 Missionaries: 1)
Current Boat Position: right


Depth:2
Current Node: 
Left:(Cannibals: 5 Missionaries: 6)
Right:(Cannibals: 1 Missionaries: 0)
Current Boat Position: left


Depth:3
Current Node: 
Left:(Cannibals: 4 Missionaries: 4)
Right:(Cannibals: 2 Missionaries: 2)
Current Boat Position: right


Depth:4
Current Node: 
Left:(Cannibals: 4 Missionaries: 6)
Right:(Cannibals: 2 Missionaries: 0)
Current Boat Position: left


Depth:5
Current Node: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: right


Depth:6
Current Node: 
Left:(Cannibals: 3 Missionaries: 6)
Right:(Cannibals: 3 Missionaries: 0)
Current Boat Position: left


Depth:7
Current Node: 
Left:(Cannibals: 1 Missionaries: 6)
Right:(Cannibals: 5 Missionaries: 0)
Current Boat Position: right


Depth:8
Current Node: 
Left:(Cannibals: 2 Missionaries: 6)
Right:(Cannibals: 4 Missionaries: 0)
Current Boat Position: left


Depth:9
Current Node: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: right


Depth:10
Current Node: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: left


Depth:11
Current Node: 
Left:(Cannibals: 3 Missionaries: 0)
Right:(Cannibals: 3 Missionaries: 6)
Current Boat Position: right


Depth:12
Current Node: 
Left:(Cannibals: 4 Missionaries: 0)
Right:(Cannibals: 2 Missionaries: 6)
Current Boat Position: left


Depth:13
Current Node: 
Left:(Cannibals: 2 Missionaries: 0)
Right:(Cannibals: 4 Missionaries: 6)
Current Boat Position: right


Depth:14
Current Node: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: left


Depth:15
Current Node: 
Left:(Cannibals: 1 Missionaries: 0)
Right:(Cannibals: 5 Missionaries: 6)
Current Boat Position: right


Depth:16
Current Node: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 5 Missionaries: 5)
Current Boat Position: left


Depth:17
Current Node: 
Left:(Cannibals: 0 Missionaries: 0)
Right:(Cannibals: 6 Missionaries: 6)
Current Boat Position: right

-------------------------------------------------------

6 Cannibals 6 Missionaries and a Boat of Capacity 5 (Question 2b)

Depth:1
Current Node: 
Left:(Cannibals: 5 Missionaries: 5)
Right:(Cannibals: 1 Missionaries: 1)
Current Boat Position: right


Depth:2
Current Node: 
Left:(Cannibals: 5 Missionaries: 6)
Right:(Cannibals: 1 Missionaries: 0)
Current Boat Position: left


Depth:3
Current Node: 
Left:(Cannibals: 4 Missionaries: 4)
Right:(Cannibals: 2 Missionaries: 2)
Current Boat Position: right


Depth:4
Current Node: 
Left:(Cannibals: 4 Missionaries: 6)
Right:(Cannibals: 2 Missionaries: 0)
Current Boat Position: left


Depth:5
Current Node: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: right


Depth:6
Current Node: 
Left:(Cannibals: 3 Missionaries: 6)
Right:(Cannibals: 3 Missionaries: 0)
Current Boat Position: left


Depth:7
Current Node: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: right


Depth:8
Current Node: 
Left:(Cannibals: 2 Missionaries: 6)
Right:(Cannibals: 4 Missionaries: 0)
Current Boat Position: left


Depth:9
Current Node: 
Left:(Cannibals: 0 Missionaries: 6)
Right:(Cannibals: 6 Missionaries: 0)
Current Boat Position: right


Depth:10
Current Node: 
Left:(Cannibals: 1 Missionaries: 6)
Right:(Cannibals: 5 Missionaries: 0)
Current Boat Position: left


Depth:11
Current Node: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 5 Missionaries: 5)
Current Boat Position: right


Depth:12
Current Node: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: left


Depth:13
Current Node: 
Left:(Cannibals: 2 Missionaries: 0)
Right:(Cannibals: 4 Missionaries: 6)
Current Boat Position: right


Depth:14
Current Node: 
Left:(Cannibals: 3 Missionaries: 0)
Right:(Cannibals: 3 Missionaries: 6)
Current Boat Position: left


Depth:15
Current Node: 
Left:(Cannibals: 1 Missionaries: 0)
Right:(Cannibals: 5 Missionaries: 6)
Current Boat Position: right


Depth:16
Current Node: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 5 Missionaries: 5)
Current Boat Position: left


Depth:17
Current Node: 
Left:(Cannibals: 0 Missionaries: 0)
Right:(Cannibals: 6 Missionaries: 6)
Current Boat Position: right

-------------------------------------------------------

'''