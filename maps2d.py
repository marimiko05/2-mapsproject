from math import ceil
import numpy as np
import json
import os

def sizeofmap():
    #функция для того, чтобы задать размер карты
    try:
        size_map = input("Введите размер карты в формате NxN и нажмите ENTER").split("x")
        size_map[0] = int(size_map[0])
        size_map[1] = int(size_map[1])
        
        return size_map
    except:
        #если пользователь вводит неправильный формат данных, то функция запускается заново
        print("Ошибка при вводе данных, введите размер карты в формате NxN, где N - натуральное число, x - латиницей")
        return sizeofmap()

def manualnewmap():
    #функция для создания ручной карты
    print("Ручное создание карты")
    size_of_map = sizeofmap()

    #вычисляем количество тайлов карты и нужно ли (и на сколько) разрезать тайлы по краям, размер каждого тайла: 16х16

    tiles_x = ceil(size_of_map[0] / 16)
    tiles_y = ceil(size_of_map[1] / 16)
    last_tile_x = size_of_map[0] % 16
    last_tile_y = size_of_map[1] % 16

    map_matrix = np.zeros((tiles_x, tiles_y), dtype=int) #создаем матрицу из нулей по заданным ранее параметрам

    map_name = str(input("Введите название карты: "))

    data_maps = {
        map_name: map_matrix.tolist()
    }
    #записываем матрицу в json-файл
    with open("map_matrixes.json", "w") as f:
        json.dump(data_maps, f)

    #цикл создания карты

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #инструкции для пользователя
        print("Введите значение для выделенного цветом тайла карты.")
        print("""\t\t0 - трава
              \t1 - начало дорожки вертикальное
              \t2 - начало дорожки горизонтальное
              \t3 - продолжение дорожки (вертикальное)
              \t4 - продолжение дорожки (горизонтальное)
              \t5 - поворот дорожки направо (верт.)
              \t6 - поворот налево (верт.)
              \t7 - поворот направо (горизонт.)
              \t8 - поворот налево (горизонт.)
              \t9 - дерево
              \t10 - куст
              \tR - сохранить изменения и скорректировать предыдущие тайлы
              \tQ - сохранить карту и выйти
              """)
        print("Изменения на карте производятся пошагово слева направо сверху вниз.")
        print("Если необходимо изменить предыдущие тайлы, введите R")

        user_choice2 = input("Ваш выбор: ")

        if user_choice2 == "q" or user_choice2 == "Q":
            break

def randomnewmap():
    print("Автоматическое создание карты")

def editmap():
    print("Редактирование карты")

menu = {
    "1" : manualnewmap,
    "2" : randomnewmap,
    "3" : editmap

}

print("""\t1 - ручное создание карты
      \t2 - автоматическое создание карты
      \t3 - редактирование уже существующей карты
      \tQ - выход
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

except Exception as e:
    print(f"Возникла ошибка: {e}")

