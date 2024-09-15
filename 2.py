num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
if num2 == 0:
 print("Деление на ноль невозможно.")
else:
  if num1 % num2 == 0:
   print(f"{num1} кратно {num2}")
  else:
   print(f"{num1} не кратно {num2}")
