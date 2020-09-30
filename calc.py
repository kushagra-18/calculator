err=["Included calculations:"]
def main():
    print('---------\nMain menu\n---------')
    print('1 - Arithmetic Operations')
    print('2 - Square Root Formula')
    print('e - for exit')
    m=input('Enter a character from the suggested: ')
    if m == '1':
        vvod()
    if m == '2':
        d(float(input('a = ')), float(input('b = ')), float(input('c = ')))
    if m == 'e':
        exit
        exit
        exit
        exit
    else:
        print('Please,enter a character from the suggested.')
        main()
def vvod():
    s[0]=(input("Enter first number or \"err\" for view a errors in this session: "))
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
    nums(s[0], s[1])
    main()
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
print('Calculator 1.3 (504) by Metrier')
def d(x, y, z):
    print("(",x,")x^2 + (",y,")x + (",z,") = 0")
    D=(y**2)-(4*x*z)
    print((-1*y+D**(1/2))/2)
    print((-1*y-D**(1/2))/2)
    main()
s=[1, 1, 1]
main()
