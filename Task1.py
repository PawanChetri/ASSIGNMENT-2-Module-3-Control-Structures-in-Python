num = int(input("Enter a number: ")) #Takes a number from user
if num%2 == 0:  #Checks if number leaves remainder 0 or not.
    print("{} is an even number.".format(num))  #If remainder is 0, it's even
else:
    print("{} is an odd number.".format(num))  #Else it is odd
