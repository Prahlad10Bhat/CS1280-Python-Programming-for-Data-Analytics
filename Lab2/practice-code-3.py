def check(num):
  if type(num) == int: 
    print("The element is an integer.")
  elif type(num) == float: 
    print("The element is a float.")
  elif type(num) == str: 
    print("The element is a string")

num=int(input("Enter an element: "))
check(num)
