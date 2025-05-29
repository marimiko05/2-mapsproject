def sizeofmap():
    try:
        size_map = input("Введите размер карты в формате NxN и нажмите ENTER").split("x")
        size_map[0] = int(size_map[0])
        size_map[1] = int(size_map[1])
        
        return size_map
    except:
        print("Ошибка при вводе данных, введите размер карты в формате NxN, где N - натуральное число, x - латиницей")
        return sizeofmap()
    

def manualnewmap():
    print("Ручное создание карты")
    size_of_map = sizeofmap()
    tiles_x = size_of_map[0] / 16
    tiles_y = size_of_map[1] / 16


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

