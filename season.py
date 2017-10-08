#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
#и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
while True:
    try:
        month = int(input("Введите номер месяца от 1 до 12 "))
        if month == 1 or month ==2 or month ==12:
            print('Это зимний месяц')
        elif month == 3 or month ==4 or month ==5:
            print('Это весенний месяц')
        elif month == 6 or month ==7 or month ==8:
            print('Это летний месяц')
        elif month == 9 or month ==10 or month ==11:
            print('Это осенний месяц')
        else:
            print("Такого месяца не существует")
    except ValueError:
        print('Необходимо ввести число ')