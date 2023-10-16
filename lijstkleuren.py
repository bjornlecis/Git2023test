import random
from colorama import Fore
lista = []
getal_gr_50 = 0
for i in range(0,20):
    x = random.randrange(1,100)
    if x > 50:
        getal_gr_50 += 1
    if x>=0 and x<=30:
        lista.append(Fore.RED + str(x) +Fore.RESET)
    elif x>=31 and x<=49:
        lista.append(Fore.YELLOW + str(x)+Fore.RESET)
    elif x>=50 and x<=75:
        lista.append(Fore.BLUE + str(x)+Fore.RESET)
    else:
        lista.append(Fore.GREEN + str(x)+Fore.RESET)

for getal in lista:
    print(getal)
print("aantal getallen groter dan 50",getal_gr_50)
