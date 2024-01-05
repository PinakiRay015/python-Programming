# python program to check the largest number among 3
def checkLargest(num1 , num2 , num3):
    if(num1 > num2):
        if(num1 > num3):
            print("{} is the largest number".format(num1))
        else:
            print("{} is the largest number".format(num3))
    else:
        if(num2 > num3):
            print("{} is the largest number".format(num2))
        else:
            print("{} is the largest number".format(num3))


checkLargest(23, 5, 101)