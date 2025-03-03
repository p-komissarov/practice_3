seconds = int(input("Введите число от 1 до 86400: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60
print(f"Текущее время: {hours} часов {minutes} минут {secs} секунд")