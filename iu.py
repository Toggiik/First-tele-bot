
from find_exel import *
# start
cost = 0
n = input("Введите кол-во  (максимально 20шт.): ")
n = int (n)
city = input("Введите город: ").lower().strip()
if city == "москва": 
    g = int(input("Если вы хотите обычную доставку нажмите 1. Если индивидуальную, нажмите 2. : "))
    if g  == 2:
        cost = serchToMoscow(n)
    elif g==1: 
        cost = serchToCity(n, city)
else: 
    cost = serchToCity(n, city)

        
        
