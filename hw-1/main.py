# @authors: 
# Burak Turksever
# Mehmet Yaylaci
# Eralp Kumbasar
import graph

choice = str(input("Would you like to run the program with the default data? (yes/no)"))
if choice.upper() == 'YES':#the program solves the 3 questions as default
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
  print("6 Cannibals 6 Missionaries and a Boat of Capacity 5")#optionally solves both of the choices in the 2nd question
  solver.DFS_start(6, 5)
elif choice.upper() == 'NO':
  while True:
    input_one = str(input('\nPlease enter the number of Missionaries and Cannibals (EXIT to exit): '))
    if input_one.upper() == 'EXIT':
      break
    else:
      if input_one.isnumeric() and int(input_one) <= 494:#check if number is above the most number of iterations possible in python
        number = int(input_one)
        input_two = str(input('Please enter the capacity of the boat: '))
        if input_two.isnumeric():
          capacity = int(input_two)
          if (capacity >= 2 and number <= 3) or ((number == 4 or number == 5) and capacity == 3) or (capacity >= 4 and number >= 6):#other combinations aren't possible as referenced in the pdf
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
Send 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 4)
Right:(Cannibals: 1 Missionaries: 1)
Current Boat Position: right


Depth:2
Return 0 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 5)
Right:(Cannibals: 1 Missionaries: 0)
Current Boat Position: left


Depth:3
Send 1 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 2 Missionaries: 2)
Current Boat Position: right


Depth:4
Return 0 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 5)
Right:(Cannibals: 2 Missionaries: 0)
Current Boat Position: left


Depth:5
Send 2 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 5)
Right:(Cannibals: 4 Missionaries: 0)
Current Boat Position: right


Depth:6
Return 1 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 5)
Right:(Cannibals: 3 Missionaries: 0)
Current Boat Position: left


Depth:7
Send 0 Cannibal(s) 3 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: right


Depth:8
Return 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 2 Missionaries: 2)
Current Boat Position: left


Depth:9
Send 0 Cannibal(s) 3 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 0)
Right:(Cannibals: 2 Missionaries: 5)
Current Boat Position: right


Depth:10
Return 1 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 0)
Right:(Cannibals: 1 Missionaries: 5)
Current Boat Position: left


Depth:11
Send 2 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 0)
Right:(Cannibals: 3 Missionaries: 5)
Current Boat Position: right


Depth:12
Return 0 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: left


Depth:13
Send 1 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 0)
Right:(Cannibals: 4 Missionaries: 5)
Current Boat Position: right


Depth:14
Return 0 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: left


Depth:15
Send 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 0 Missionaries: 0)
Right:(Cannibals: 5 Missionaries: 5)
Current Boat Position: right

-------------------------------------------------------

6 Cannibals 6 Missionaries and a Boat of Capacity 4 (Question 2a)

Depth:1
Send 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 5 Missionaries: 5)
Right:(Cannibals: 1 Missionaries: 1)
Current Boat Position: right


Depth:2
Return 0 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 5 Missionaries: 6)
Right:(Cannibals: 1 Missionaries: 0)
Current Boat Position: left


Depth:3
Send 1 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 4)
Right:(Cannibals: 2 Missionaries: 2)
Current Boat Position: right


Depth:4
Return 0 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 6)
Right:(Cannibals: 2 Missionaries: 0)
Current Boat Position: left


Depth:5
Send 1 Cannibal(s) 3 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: right


Depth:6
Return 0 Cannibal(s) 3 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 6)
Right:(Cannibals: 3 Missionaries: 0)
Current Boat Position: left


Depth:7
Send 2 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 6)
Right:(Cannibals: 5 Missionaries: 0)
Current Boat Position: right


Depth:8
Return 1 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 6)
Right:(Cannibals: 4 Missionaries: 0)
Current Boat Position: left


Depth:9
Send 0 Cannibal(s) 4 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: right


Depth:10
Return 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: left


Depth:11
Send 0 Cannibal(s) 3 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 0)
Right:(Cannibals: 3 Missionaries: 6)
Current Boat Position: right


Depth:12
Return 1 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 0)
Right:(Cannibals: 2 Missionaries: 6)
Current Boat Position: left


Depth:13
Send 2 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 0)
Right:(Cannibals: 4 Missionaries: 6)
Current Boat Position: right


Depth:14
Return 0 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: left


Depth:15
Send 1 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 0)
Right:(Cannibals: 5 Missionaries: 6)
Current Boat Position: right


Depth:16
Return 0 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 5 Missionaries: 5)
Current Boat Position: left


Depth:17
Send 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 0 Missionaries: 0)
Right:(Cannibals: 6 Missionaries: 6)
Current Boat Position: right

-------------------------------------------------------

6 Cannibals 6 Missionaries and a Boat of Capacity 5 (Question 2b)

Depth:1
Send 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 5 Missionaries: 5)
Right:(Cannibals: 1 Missionaries: 1)
Current Boat Position: right


Depth:2
Return 0 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 5 Missionaries: 6)
Right:(Cannibals: 1 Missionaries: 0)
Current Boat Position: left


Depth:3
Send 1 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 4)
Right:(Cannibals: 2 Missionaries: 2)
Current Boat Position: right


Depth:4
Return 0 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 4 Missionaries: 6)
Right:(Cannibals: 2 Missionaries: 0)
Current Boat Position: left


Depth:5
Send 1 Cannibal(s) 3 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 3)
Right:(Cannibals: 3 Missionaries: 3)
Current Boat Position: right


Depth:6
Return 0 Cannibal(s) 3 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 6)
Right:(Cannibals: 3 Missionaries: 0)
Current Boat Position: left


Depth:7
Send 1 Cannibal(s) 4 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: right


Depth:8
Return 0 Cannibal(s) 4 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 6)
Right:(Cannibals: 4 Missionaries: 0)
Current Boat Position: left


Depth:9
Send 2 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 0 Missionaries: 6)
Right:(Cannibals: 6 Missionaries: 0)
Current Boat Position: right


Depth:10
Return 1 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 6)
Right:(Cannibals: 5 Missionaries: 0)
Current Boat Position: left


Depth:11
Send 0 Cannibal(s) 5 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 5 Missionaries: 5)
Current Boat Position: right


Depth:12
Return 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 2)
Right:(Cannibals: 4 Missionaries: 4)
Current Boat Position: left


Depth:13
Send 0 Cannibal(s) 2 Missionary(ies)
Current State: 
Left:(Cannibals: 2 Missionaries: 0)
Right:(Cannibals: 4 Missionaries: 6)
Current Boat Position: right


Depth:14
Return 1 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 3 Missionaries: 0)
Right:(Cannibals: 3 Missionaries: 6)
Current Boat Position: left


Depth:15
Send 2 Cannibal(s) 0 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 0)
Right:(Cannibals: 5 Missionaries: 6)
Current Boat Position: right


Depth:16
Return 0 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 1 Missionaries: 1)
Right:(Cannibals: 5 Missionaries: 5)
Current Boat Position: left


Depth:17
Send 1 Cannibal(s) 1 Missionary(ies)
Current State: 
Left:(Cannibals: 0 Missionaries: 0)
Right:(Cannibals: 6 Missionaries: 6)
Current Boat Position: right

-------------------------------------------------------

'''