from tkinter import *
from tkinter import messagebox
import json
import numpy as np
from math import ceil

def error1():
    #диалоговое окно показывающее ошибку
    messagebox.showerror(title="Ошибка!", message="Введите данные в корректном формате")

def mapmatrixzeros(size_map):

    #функция создающая матрицу из нулей для карты

    global tiles_x, tiles_y

    tiles_x = ceil(size_map[0] / 16)
    tiles_y = ceil(size_map[1] / 16)

    map_matrix = np.zeros((tiles_x, tiles_y), dtype=int)

    return map_matrix

def manualmapcreate(size_map,namemap):

    map_matrix = mapmatrixzeros(size_map)

    data_maps ={
        namemap: map_matrix.tolist()
    }

    #записываем данные в json-файл

    # try:
    #     with open("map_matrixes.json", "r") as f:
    #         data = json.load(f)

    # except FileNotFoundError:
    #     data = []

    # data.append(data_maps)

    # with open("map_matrixes.json", "w") as f:
    #     json.dump(data, f, indent=2)

    manualmapwindow2 = Tk()
    #новое окно с непосредственно настройкой карты

    manualmapwindow.destroy()
    print(tiles_y, tiles_x)

    frame = Frame(manualmapwindow2)
    frame.place(x=0,y=0)
    
    empty_tile = PhotoImage(file='map_assets/empty_tile.png')

    for i in range(tiles_x):
        for j in range(tiles_y):
            tile_button = Button(text={map_matrix[i][j].item()},
                                 image=empty_tile)
            tile_button.grid(row=i, column=j)


def submitsettingsbutton():
    #проверка формата введенных данных
    sizeinput = sizemapentry.get()
    namemap = nameofmap.get()
    try:
        size_map = sizeinput.split("x")
        size_map[0] = int(size_map[0])
        size_map[1] = int(size_map[1])

    except:
        error1()

    else:
        #проверка имени карты на латиницу, числа, тире, нижнее подчеркивание
        for i in namemap:
            if (ord(i) >= 48 and ord(i) <= 57) or (ord(i) >=65 and ord(i) <=90) or (ord(i) >= 97 and ord(i) <= 122) or ord(i) == 45 or ord(i) == 95:
                acceptname = True
            else:
                acceptname = False
                  
        if not acceptname:
            error1()
        else:
            manualmapcreate(size_map,namemap)
                

def manualnewmap():
    #окно для настроек ручного режима
    global manualmapwindow, sizemapentry, nameofmap
    manualmapwindow = Tk()
    mainmenuwindow.destroy()

    headline2 = Label(manualmapwindow,
                      text = "Настройки карты",
                      font = ("Pixelify Sans",40), 
                      fg ="#639bff", 
                      bg ="#b9d2ff",
                      relief=RAISED,
                      bd = 10,
                      padx = 10,
                      pady = 10).pack()
    
    instructions1 = Label(manualmapwindow,
                          text = "Введите размер карты в формате NxN, где N - натуральное число",
                          font = ("Pixelify Sans",30)).pack(pady=5)
    
    sizemapentry = Entry(manualmapwindow,
                         font = ("Pixelify Sans",30),
                         )
    sizemapentry.pack(pady=5)

    instructions2 = Label(manualmapwindow,
                          text = "Введите название карты на латинице без пробелов",
                          font = ("Pixelify Sans",30)).pack(pady=5)
    
    nameofmap = Entry(manualmapwindow,
                         font = ("Pixelify Sans",30),
                         )
    nameofmap.pack(pady=5)

    submitsettings = Button(manualmapwindow, 
                        text = "Сохранить",
                        command = submitsettingsbutton).pack(pady=5)
    
    manualmapwindow.mainloop()

mainmenuwindow = Tk()

#первое окно, где пользователь выбирает что будет изначально делать

headline1 = Label(mainmenuwindow, 
            text = "Генератор карты",
            font = ("Pixelify Sans",40), 
            fg ="#639bff", 
            bg ="#b9d2ff",
            relief=RAISED,
            bd = 10,
            padx = 10,
            pady = 10
            )

headline1.pack()

#кнопка открывает ручной режим
buttonmanualgen = Button(mainmenuwindow,
                         text = "Ручное создание карты",
                         command=manualnewmap,
                         font = ("Pixelify Sans",40),
                         state = ACTIVE,
                         compound = 'left'
                         )
buttonmanualgen.pack()

#кнопка открывает меню создания рандомной карты
buttonrandomgen = Button(mainmenuwindow,
                         text = "Автоматическое создание карты",
                         #command=randomnewmap,
                         font = ("Pixelify Sans",40),
                         state = ACTIVE,
                         compound = 'left'
                         )
buttonrandomgen.pack()

#редактирование уже существующей карты
buttoneditmap = Button(mainmenuwindow,
                       text = "Редактирование карты",
                       #command=editmap,
                       font = ("Pixelify Sans",40),
                       state = ACTIVE,
                       compound = 'left').pack()

mainmenuwindow.mainloop()

