from colorama import Fore
import math
print(Fore.LIGHTRED_EX+"ax^2+"+Fore.LIGHTCYAN_EX+"bx+"+Fore.LIGHTGREEN_EX+"c=0")
a=int(input(Fore.LIGHTYELLOW_EX+"Please Enter a number:"))
b=int(input(Fore.LIGHTYELLOW_EX+"Please Enter b number:"))
c=int(input(Fore.LIGHTYELLOW_EX+"Please Enter c number:"))
print(Fore.LIGHTMAGENTA_EX+"Delta=b^2-4ac")
delta=(b*b)-(4*a*c)
print(Fore.LIGHTWHITE_EX+str(delta))
if delta>0:
   x1=((-1*b)-math.sqrt(delta))/(2+a)
   x2=((-1*b)+math.sqrt(delta))/(2+a)
   print(Fore.CYAN+"X1: " + str(x1) + Fore.GREEN+" X2: " +str(x2))
elif delta==0:
   print(Fore.LIGHTCYAN_EX+"x=-b/2a")
   x=(-1*b)/(2+a)
   print(Fore.YELLOW+str(x))
else:
   print(Fore.RED+"No Root")