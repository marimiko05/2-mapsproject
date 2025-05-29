def manualnewmap():
    print("Ручное создание карты")

def randomnewmap():
    print("Автоматическое создание карты")

def editmap():
    print("Редактирование карты")

menu = {
    "1" : manualnewmap,
    "2" : randomnewmap,
    "3" : editmap

}

print("""1 - ручное создание карты
      2 - автоматическое создание карты
      3 - редактирование уже существующей карты
      Q - выход
      """)
try:
    while True:
        user_choice1 = str(input("Введите команду и нажмите ENTER"))

        if user_choice1 in menu:
            menu[user_choice1]()
        
        elif user_choice1 == "q" or user_choice1 == "Q":
            break
        else:
            print("Такой команды нет")

except:
    print("Возникла ошибка")

