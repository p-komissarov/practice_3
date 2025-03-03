att = int(input("Введите ATT: "))
comp = int(input("Введите COMP: "))
yds = int(input("Введите YDS: "))
td = int(input("Введите TD: "))
int = int(input("Введите INT: "))
a = (comp / att - 0.3) * 5
b = (yds / att - 3) * 0.25
c = (td / att) * 20
d = 2.375 - (int / att * 25)
print("Passer Rating: ", ((a + b + c + d) / 6) * 100)