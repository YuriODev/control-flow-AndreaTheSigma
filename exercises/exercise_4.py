# Your solution to Exercise 4
grade = int(input("Enter the grade: "))
if grade == 1 or grade == 2 or grade == 3:
  print("initial level")
elif grade == 4 or grade == 5 or grade == 6:
  print("average level")
elif grade == 7 or grade == 8 or grade == 9:
  print("sufficient level")
elif grade == 10 or grade == 11 or grade == 12:
  print("high level")
else:
  print ("level is absent")