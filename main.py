import add 
import sub
import Multiply
import DIV
x=int(input("Please Enter The first Number: "))
y=int(input("Please Enter The second Number: "))

a=int(input("Choose option:\n 1. Add\n 2.Substract\n 3.Multiply\n 4.Divide"))

if a==1:
  print("The sum of the 2 numbers is:",add.add(x,y))
if a==2:
  print("The difference of the 2 numbers is:",sub.sub(x,y))
if a==3:
  print("The product of the 2 numbers is:",Multiply.multiply(x,y))
if a==4:
  print("The quotient of the 2 numbers is:",DIV.divide(x,y))
