#Programm for Termux!
#For sololearn's inhabitans:
#you must enter numbers like this:
#4
#2
#but if you enter after the numbers any key, but not "y", the program will close without error.
def vvod():
    try:
        s[0]=float(input("Enter first number: "))
        s[1]=float(input("Enter second number: "))
    except ValueError:
        print("Value error! Enter a NUMBER.")
        vvod()
    if s[0] == 0 or s[1] == 0:
        print("\nPlease exclude zero.")
        vvod()
    else:
        print("\nAnswers:")
        nums(s[0], s[1])

    print("Return to enter numbers?\n(y/press enter)")
    ex = input()
    if ex == "y" or ex == "yes":
       vvod()
    else:
       exit
def nums(x, y):
    print(x,"+",y,"=",x+y)
    print(x,"-",y,"=",x-y)
    print(x,"*",y,"=",x*y)
    print(x,"/",y,"=",x/y)
    try:
        print(x,"^",y,"=",x**y)
    except:
        print(x,"^",y,"= very long number")
    print(y,"degree root of",x,"=",x**(1/y))
    print("-------Reverse numbers-------")
    print(y,"-",x,"=",y-x)
    print(y,"/",x,"=",y/x)
    try:
        print(y,"^",x,"=",y**x)
    except:
        print(y,"^",x,"= very long number")
    print (x,"degree root of",y,"=",y**(1/y))
s=[0, 0]
vvod()