from random import randint 
x = randint(1,3)
number = int(input())
if (x == 1):
    print ("the computer choose rock")
elif (x == 2):
    print ("the computer choose paper")
elif (x == 3):
    print ("the computer choose scissors")



if (number == 1):
    print ("you choose rock")
elif (number == 2):
    print ("you choose paper")
elif (number == 3):
    print ("you choose scissors")


print (x)
print (number)



if (x == 1 and number == 2):
    print ("you win") 
elif (x == 1 and number == 3):
    print ("you lost")
elif (x == 1 and number ==1):
    print ("you tied")
elif (x == 2 and number == 1):
    print ("you lost")
elif (x == 2 and number == 2):
    print ("you tied")
elif (x == 2 and number == 3):
    print ("you win")
elif (x == 3 and number == 1):
    print ("you win")
elif (x == 3 and number == 2):
    print ("you lose")
elif (x == 3 and number == 3):
    print ("you tied")