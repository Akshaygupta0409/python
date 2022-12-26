# Write a program to accept an integer from the user and display all the numbers from 1 to that number. Repeat the process until the user enters 0.
valid = True

while valid:
    x = int(input("Enter the number :"))
    if x != 0:
      i=1
      while i<=x:
        print(i , end=" ")
        i = i+1
        print("\n")
    else:
        valid = False


