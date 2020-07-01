import re


print("Our magical calculator")
print("type quit to stop thee calculator\n")


previous = 0
run = True

def performMath():
    global run
    global previous
    if previous == 0:
        equation = input("enter the equation correctly: ")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Good bye...")
        run = False
    else:
        equation = re.sub('[a-zA-Z.,;:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)





while run:
    performMath()