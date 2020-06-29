"""
******this piece of code is used to learn how function works.******

def my_anotherfunc(str1, str2):
    print(str1)
    print(str2)

my_anotherfunc("this is neel", "learning pthon")
my_anotherfunc("hello", "who is this")

**** this shows how the functuon can have arguments keyword. ****
def my_print(name = "someone", age = "unknown"):
    print("my name is", name, "and my age is", age)

my_print("nick")



def my_print(name = "someone", age = "unknown"):
    print("my name is", name, "and my age is", age)

my_print(None, 27)      # you an also overwrote age by doing (age = 12) in the parameter. and same way the nam can also be changed if not given.





def print_people(*people):       #the *people will include objects from the array provided.
    for person in people:
        print("this person is : ", person)

print_people("Nick", "sam", "heven", "jay")



def do_math(num1, num2):
    return num1 +num2

math1 = do_math(3,5)
math2 = do_math(7,9)

print("this is tital for ", math1, ", and this is total for ",math2)



#this is if else conditions tutorial.

check = True

if check == False:
    print("It is false")

elif check == "hamburger":
    print("yummmmm, hamburgers")

elif check == "yo":
    print("hello")

else:
    print("this is actually True.")


# example of for and while loops and how they work in python.

numbers = ["nick", "patel", "george", "sam"]

for item in numbers:
    print("tis person is " ,item)


run = True
current = 1

while run:
    if current == 100:
        run = False

    else:
        print(current)
        current +=1

"""

