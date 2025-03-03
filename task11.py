angle = float(input("Введите угол наклона стрелки: "))
hours = int(angle // 30)
minutes = int((angle % 30) * 2)
print(f"С начала суток прошло {hours} часов {minutes} минут")