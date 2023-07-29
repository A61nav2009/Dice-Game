import random
response = "y"

response=(input("Do you want to roll a dice or not?, Answer with y for yes or n for no"))



while response == "y":
    no = random.randint(1,6)
    if no==1:
        print("the value you rolled is 1")
    if no==2:
        print("the value you rolled is 2")
    if no==3:
        print("the value you rolled is 3")
    if no==4:
        print("the value you rolled is 4")
    if no==5:
        print("the value you rolled is 5")
    if no==6:
        print("the value you rolled is 6")

    response=(input("Do you want to roll a dice again, Answer with y for yes or n to exit"))



