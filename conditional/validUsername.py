# python program to cheeck weather a username is valid or not
def userName(name):
    if len(name) < 3:
        print("This Username is not valid")
    else:
        print("You are good to go")


userName("Rohan")
