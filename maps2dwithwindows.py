from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
import numpy as np
from PIL import Image, ImageTk
from math import ceil

#ссылки на файлы
global tiles_dictionary

tiles_dictionary = {
    "path": {
        "path1": ['map_assets/grasstype2road3.png', 1],
        "path2": ['map_assets/grasstype2roadturn1.png', 2],
        "path3": ['map_assets/grasstype2roadturn4.png', 3],
        "path4": ['map_assets/pathmud.png', 4],
        "path5": ['map_assets/pathmud2.png', 5],
        "path6": ['map_assets/pathmud3.png', 6],
        "path7": ['map_assets/pathmud4.png', 7]
    },
    "bushes": {
        'bushes1': ['map_assets/grass1.png', 8],
        'bushes2': ['map_assets/grassandbushes1.png', 9],
        'bushes3': ['map_assets/grassandbushes3.png', 10],
        'bushes4': ['map_assets/grassandbushes4.png', 11],
        'bushes5': ['map_assets/grasswithflower.png', 12],
        'bushes6': ['map_assets/pathmudhorizontaledge.png', 13],
        'bushes7': ['map_assets/pathturndown.png', 14],
        'bushes8': ['map_assets/pathturninner1.png', 15]

    },
    "water": {
        'water1': ['map_assets/water1.png', 16],
        'water2': ['map_assets/water2.png', 17],
        'water3': ['map_assets/water3.png', 18],
        'water4': ['map_assets/waterbushes1.png', 19],
        'water5': ['map_assets/waterbushes2.png', 20],
        'water6': ['map_assets/waterbushes3.png', 21],
        'water7': ['map_assets/waterbushes4.png', 22],
        'water8': ['map_assets/waterbushes5.png', 23],
        'water9': ['map_assets/waterbushes6.png', 24],
        'water10': ['map_assets/waterbushes7.png', 25],
        'water11': ['map_assets/waterbushes8.png', 26],
        'water12': ['map_assets/watergrass1.png', 27],
        'water13': ['map_assets/watergrass2.png', 28],
        'water14': ['map_assets/watergrass3.png', 29],
        'water15': ['map_assets/watergrass4.png', 30],
        'water16': ['map_assets/watergrass5.png', 31],
        'water17': ['map_assets/watergrass6.png', 32],
        'water18': ['map_assets/watergrass7.png', 33], 
        'water19': ['map_assets/watergrass8.png', 34],
        'water20': ['map_assets/waterpath1.png', 35],
        'water21': ['map_assets/waterpath2.png', 36],
        'water22': ['map_assets/waterpath3.png', 37],
        'water23': ['map_assets/waterpath4.png', 38],
        'water24': ['map_assets/waterpath5.png', 39],
        'water25': ['map_assets/waterpath6.png', 40]
    },
    "grass": {
        'grass1': ['map_assets/alotofgrass.png', 41], 
        'grass2': ['map_assets/grasstype2full.png', 42],
        'grass3': ['map_assets/grasstype2road2.png', 43],
        'grass4': ['map_assets/grasstype2roadturn2.png', 44],
        'grass5': ['map_assets/grasstype2roadturn3.png', 45],
        'grass6': ['map_assets/grasstype2roadturn3.png', 46]
    },
    "trees": {
        'smallbush1': ['map_assets/smallbush1.png', 48],
        'smallbush2': ['map_assets/smallbush2.png', 49],
        'smallbush3': ['map_assets/smallbush3.png', 50],
        'smallbush4': ['map_assets/smallbush4.png', 51],
        'tree1': ['map_assets/tree1.png', 52],
        'tree2': ['map_assets/tree2.png', 53],
        'tree3': ['map_assets/tree3.png', 54],
        'tree4': ['map_assets/tree4.png', 55],
        'tree5': ['map_assets/tree5.png', 56],
        'tree6': ['map_assets/tree6.png', 57],
        'tree7': ['map_assets/tree7.png', 58],
        'tree8': ['map_assets/tree8.png', 59],
        'tree9': ['map_assets/tree9.png', 60],
        'tree10': ['map_assets/tree10.png', 61],
        'tree11': ['map_assets/tree11.png', 62]
    }
}

#кнопка выбора тайла на матрице

# def choosetileonmatrix():
#     print("position:")

#кнопка выбора тайла с картинкой
def choosetile():
    print("!")
#кнопка выбора тайла
def radiobuttonselector(dictionary, key1, window):
    try:
        global user_choice_tile

        user_choice_tile = IntVar()

        for i in dictionary[key1]:
            icon = PhotoImage(file=dictionary[key1][i][0])
            tilecode = dictionary[key1][i][1]
            radiobutton = Radiobutton(window,
                                  variable = user_choice_tile,
                                  value=tilecode,
                                  image=icon)
            radiobutton.pack(anchor=W)
            radiobutton.image = icon
    
    except Exception as e:
        print(e)

    selecttilebutton = Button(window,
                              text = "Выбрать тайл",
                              #command=choosetile,
                              font = ("Pixelify Sans",20),
                              state = ACTIVE,
                              compound = 'left')
    selecttilebutton.pack()


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

def manualmapcreate(size_map,namemap, tiles_dictionary):

    map_matrix = mapmatrixzeros(size_map)

    # data_maps ={
    #     namemap: map_matrix.tolist()
    # }
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
    #матрица с пустыми тайлами

    frame = Frame(manualmapwindow2)
    frame.place(x=0,y=0)
    
    empty_tile = PhotoImage(file='map_assets/empty_tile.png')

    for i in range(tiles_x):
        for j in range(tiles_y):
            
            tile_button = Button(text={map_matrix[i][j].item()},
                                #  command=get_coordinates,
                                 image=empty_tile)
            
            tile_button.grid(row=i, column=j)
            tile_button.image = empty_tile

    manualinstructions = Label(manualmapwindow2,
                               text = "Нажмите на тайл выше и выберите изображение внизу",
                               font = ("Pixelify Sans",30))

    if (tiles_y*16) >= 320:
        manualinstructions.grid(row = tiles_x+1, column = 0, columnspan=(tiles_y*16-49), sticky = 'w')

    else:
        manualinstructions.grid(row = tiles_x+1, column = 0, columnspan=320, sticky = 'w')

    #меню выбора тайла
    choosetypeoftile = ttk.Notebook(manualmapwindow2)

    pathtiles = Frame(choosetypeoftile)
    bushestiles = Frame(choosetypeoftile)
    watertiles = Frame(choosetypeoftile)
    grasstiles = Frame(choosetypeoftile)
    treestiles = Frame(choosetypeoftile)
    
    choosetypeoftile.add(pathtiles, text="Дорога")
    choosetypeoftile.add(bushestiles, text="Заросли")
    choosetypeoftile.add(watertiles, text="Вода")
    choosetypeoftile.add(grasstiles, text="Трава")
    choosetypeoftile.add(treestiles, text="Деревья")

    choosetypeoftile.grid(row=tiles_x + 2, column = 0, columnspan= 320, sticky = 'w')

    radiobuttonselector(tiles_dictionary,'path',pathtiles)
    radiobuttonselector(tiles_dictionary,'bushes',bushestiles)
    radiobuttonselector(tiles_dictionary,'water', watertiles)
    radiobuttonselector(tiles_dictionary,'grass', grasstiles)
    radiobuttonselector(tiles_dictionary,'trees', treestiles)



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
            manualmapcreate(size_map,namemap,tiles_dictionary)
                

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

