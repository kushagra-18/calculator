def nums(x, y):
   print(x,"+",y,"=",x+y)
   print(x,"-",y,"=",x-y)
   print(x,"*",y,"=",x*y)
   print(x,"/",y,"=",x/y)
   print(x,"^",y,"=",x**y)
   print()
s = [0, 0]
def vvod():
   s[0] = float(input("Enter first num: "))
   s[1] = float(input("\nEnter second num: "))
   if not s[1] == 0:
       print("\nAnswers:")
       nums(s[0], s[1])
   else:
       print("\nHello world!")

   print("Return to enter nums?\n(y/press enter)")
   ex = input()
   if ex == "y" or ex == "yes":
      vvod()
   else:
      exit
vvod()
