def checkLargestNum(num1, num2, num3):
    if num1 > num3 and num1 > num2:
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        return num3


print(checkLargestNum(112, 44, 222))
