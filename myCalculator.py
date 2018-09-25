import re

flag = True
equation = ""
check = 0


def operation():
    global equation
    global check
    global flag

    if equation == "":
        check = input("Type your equation: ")
        if check == "quit":
            flag = False
            return None
        check = re.sub("[A-Za-z' ']", "", check )
        equation = eval(check)
    else:
        check = str(input(str(equation) + " "))
        if check == "quit":
            flag = False
            return None
        check = re.sub("[A-Za-z' ']", "", check)
        equation = eval(str(equation) + check)


while flag:
    operation()
