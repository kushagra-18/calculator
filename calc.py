#Programm for Termux!
#For sololearn's inhabitans:
#you must enter numbers like this:
#4
#2
#but if you enter after the numbers any key, but not "y", the program will close without error.
err=["Included calculations:"]
def ent():
    x=input()
    if x == "y":
        vvod()
    else:
        exit
def vvod():
    s[0]=input("Enter first number or \"err\" for view a errors in this session: ")
    if s[0] == "err":
        for i in range(len(err)):
            print(err[i])
        vvod()
    s[1]=input("Enter second number: ")
    try:
        s[0]=float(s[0])
        s[1]=float(s[1])
    except ValueError:
        print("Value error! Enter a NUMBER.")
        vvod()
    if s[0] == 0 or s[1] == 0:
        print("\nPlease exclude zero.")
        vvod()
    else:
        print("\nAnswers:")
        nums(s[0], s[1])
    print("-----------------------------------------------\nFor exit from calculator press CTRL+D or CTRL+c\n-----------------------------------------------")
    vvod()
def nums(x, y):
    print("1.",x,"+",y,"=",x+y)
    print("2.",x,"-",y,"=",x-y)
    print("3.",x,"*",y,"=",x*y)
    print("4.",x,"/",y,"=",x/y)
    try:
        print("5.",x,"^",y,"=",x**y)
    except:
        err.append("5. <<Very long number.")
    print("6.",y,"degree root of",x,"=",x**(1/y))
    print("7.",x,"! =",fact(x, 7))
    print("-------Reverse numbers-------")
    print("8.",y,"-",x,"=",y-x)
    print("9.",y,"/",x,"=",y/x)
    try:
        print("10.",y,"^",x,"=",y**x)
    except:
        err.append("10. <<Very long number")
    print("11.",x,"degree root of",y,"=",y**(1/y))
    print("12.",y,"! =",fact(y, 12))
def fact(x, y):
    try:
        if x==1:
            return 1
        else:
            return float(x*fact(x-1))
    except:
        return('calculator have got autism!')
        if y == 7:
            err.append("7. <<Very long number.")
        else:
            err.append("12. <<Very long number.")

s=[1,1]
vvod()
