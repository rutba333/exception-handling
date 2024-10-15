valid=False
while not valid:#using nested while loop
    try:
     n=int(input("Enter a even number"))
     while n%2==0:

      print("bye")
      valid=True
    except ValueError:
      print("invalid input")