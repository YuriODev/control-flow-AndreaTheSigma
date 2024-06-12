# Your solution to Exercise 3
number = int(input("Enter a number between 0-36: "))
if number == 0:
  print("Green")
elif number >=1 and number <=10:
  if number % 2 == 0:
    print("Black")
  else:
    print("Red")
elif number >=11 and number <=18:
  if number % 2 == 0:
    print("Red")
  else:
    print("Black")
elif number >=19 and number <=28:
  if number % 2 == 0:
    print("Black")
  else:
    print("Red")
elif number >=29 and number <=36:
  if number % 2 == 0:
    print("Red")
  else:
    print("Black")
else:
  print("The bet will not play!")