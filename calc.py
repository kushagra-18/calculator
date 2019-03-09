def nums(x, y):
   print(x,"+",y,"=",x+y)
   print(x,"-",y,"=",x-y)
   print(x,"*",y,"=",x*y)
   print(x,"/",y,"=",x/y)
   print()
s = [0, 0]
print("Enter first num")
s[0] = int(input())
print("Enter second num")
s[1] = int(input())
if not s[0] == 0 and not s[1] == 0:
    print("Answers")
    nums(s[0], s[1])
else:
    print("Actions with zero are meaningless")