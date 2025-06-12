from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import json
import numpy as np
from PIL import Image, ImageTk
from math import ceil

#ссылки на файлы
global tiles_dictionary, rotations

rotations = {}

tiles_dictionary = {
    "path": {
        "1": 'map_assets/grasstype2road3.png',
        "2": 'map_assets/grasstype2roadturn1.png',
        "3": 'map_assets/grasstype2roadturn4.png',
        "4": 'map_assets/pathmud.png',
        "5": 'map_assets/pathmud2.png',
        "6": 'map_assets/pathmud3.png',
        "7": 'map_assets/pathmud4.png'
    },
    "bushes": {
        '8': 'map_assets/grass1.png',
        '9': 'map_assets/grassandbushes1.png',
        '10': 'map_assets/grassandbushes3.png',
        '11': 'map_assets/grassandbushes4.png',
        '12': 'map_assets/grasswithflower.png',
        '13': 'map_assets/pathmudhorizontaledge.png',
        '14': 'map_assets/pathturndown.png',
        '15': 'map_assets/pathturninner1.png'

    },
    "water": {
        '16': 'map_assets/water1.png',
        '17': 'map_assets/water2.png',
        '18': 'map_assets/water3.png',
        '19': 'map_assets/waterbushes1.png',
        '20': 'map_assets/waterbushes2.png',
        '21': 'map_assets/waterbushes3.png',
        '22': 'map_assets/waterbushes4.png',
        '23': 'map_assets/waterbushes5.png',
        '24': 'map_assets/waterbushes6.png',
        '25': 'map_assets/waterbushes7.png',
        '26': 'map_assets/waterbushes8.png',
        '27': 'map_assets/watergrass1.png',
        '28': 'map_assets/watergrass2.png',
        '29': 'map_assets/watergrass3.png',
        '30': 'map_assets/watergrass4.png',
        '31': 'map_assets/watergrass5.png',
        '32': 'map_assets/watergrass6.png',
        '33': 'map_assets/watergrass7.png', 
        '34': 'map_assets/watergrass8.png',
        '35': 'map_assets/waterpath1.png',
        '36': 'map_assets/waterpath2.png',
        '37': 'map_assets/waterpath3.png',
        '38': 'map_assets/waterpath4.png',
        '39': 'map_assets/waterpath5.png',
        '40': 'map_assets/waterpath6.png'
    },
    "grass": {
        '41': 'map_assets/alotofgrass.png',
        '42': 'map_assets/grasstype2full.png',
        '43': 'map_assets/grasstype2road2.png',
        '44': 'map_assets/grasstype2roadturn2.png',
        '45': 'map_assets/grasstype2roadturn3.png',
        '46': 'map_assets/grasstype2roadturn3.png'
    },
    "trees": {
        '48': 'map_assets/smallbush1.png',
        '49': 'map_assets/smallbush2.png',
        '50': 'map_assets/smallbush3.png',
        '51': 'map_assets/smallbush4.png',
        '52': 'map_assets/tree1.png',
        '53': 'map_assets/tree2.png',
        '54': 'map_assets/tree3.png',
        '55': 'map_assets/tree4.png',
        '56': 'map_assets/tree5.png',
        '57': 'map_assets/tree6.png',
        '58': 'map_assets/tree7.png',
        '59': 'map_assets/tree8.png',
        '60': 'map_assets/tree9.png',
        '61': 'map_assets/tree10.png',
        '62': 'map_assets/tree11.png'
    }
}


def savemap():

    resultimage = createimagemap()

    file_path = filedialog.askdirectory()

    if file_path:
        resultimage.save(f"{file_path}/{namemap}.png")

        data_maps = {
        'map_matrix': map_matrix.tolist(),
        'rotate': rotations
        
    }
    # записываем данные в json-файл

        try:
            with open("map_matrixes.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            data =  {}

        data[namemap] = data_maps

        with open("map_matrixes.json", "w") as f:
            json.dump(data, f, indent=2)

        modifymapwindow.destroy()
        manualmapwindow2.destroy()

        
    else:
        if messagebox.askokcancel(title="Ошибка!", message="Папка для сохранения не выбрана. Выберите папку"):
            return savemap
        else:
            messagebox.showerror(title="Ошибка!", message="Файл карты не сохранен")

def nexttilebutton():
    modifymapwindow.destroy()

def updateimage():
    mapimage = createimagemap()
    tk_im_map2 = ImageTk.PhotoImage(mapimage)
    pict_map.image = tk_im_map2
    pict_map.config(image=tk_im_map2)

def tilerotation1():
    rotations[position] = 90
    updateimage()

def tilerotation2():
    rotations[position] = 180
    updateimage()
 
def tilerotation3():
    rotations[position] = 270
    updateimage()
    
def tilerotation4():
    if position in rotations:
        del rotations[position]
    updateimage()
  
def createimagemap():
                 
    mapfile = Image.new("RGB", (main_y, main_x))

    for i in range(tiles_x):
        for j in range(tiles_y):

            strposition = str(i) + " " + str(j)

            if map_matrix[i][j] == 0:
                tile = Image.open('map_assets/empty_tile.png')
            elif str(map_matrix[i][j]) in tiles_dictionary['bushes']:
                tile = Image.open(tiles_dictionary['bushes'][str(map_matrix[i][j])])
            elif str(map_matrix[i][j]) in tiles_dictionary['path']:
                tile = Image.open(tiles_dictionary['path'][str(map_matrix[i][j])])
            elif str(map_matrix[i][j]) in tiles_dictionary['water']:
                tile = Image.open(tiles_dictionary['water'][str(map_matrix[i][j])])
            elif str(map_matrix[i][j]) in tiles_dictionary['grass']:
                tile = Image.open(tiles_dictionary['grass'][str(map_matrix[i][j])])
            elif str(map_matrix[i][j]) in tiles_dictionary['trees']:
                tile = Image.open(tiles_dictionary['trees'][str(map_matrix[i][j])])

            if (crop_x != 0 or crop_y != 0) and (i == (tiles_x - 1) or j == (tiles_y - 1)):
            
                if j == (tiles_y - 1) and i == (tiles_x - 1):
                    crop_x_fin = 16
                    crop_y_fin = 16
                    if crop_x>0:
                        crop_x_fin = crop_x
                    if crop_y>0:
                        crop_y_fin = crop_y
                    box = (0, 0,crop_y_fin,crop_x_fin)

                elif i == (tiles_x - 1):
                    crop_x_fin = 16
                    if crop_x>0:
                        crop_x_fin = crop_x
                    box = (0, 0, 16, crop_x_fin)
                    
                elif j == (tiles_y - 1):
                    crop_y_fin = 16
                    if crop_y>0:
                        crop_y_fin = crop_y
                    box = (0, 0, crop_y_fin, 16)          
            
                tile = tile.crop(box)

            if strposition in rotations:
                anglenum = rotations[strposition]
                tile = tile.rotate(anglenum)

            mapfile.paste(tile, (0+j*16, 0+i*16))

    # mapfile.show()

    return mapfile

#кнопка выбора тайла на матрице

def choosetileonmatrix(event):
    global position
    position = event.widget.cget("text")

    
#кнопка выбора тайла с картинкой
def choosetile(t):
    global chosentile
    chosentile = t

def modifymap():

    try:

        temp_position = position.split()
        temp_x = int(temp_position[0])
        temp_y = int(temp_position[1])

        map_matrix[temp_x, temp_y] = chosentile

    except:
        error2()

    else:
        global modifymapwindow

        modifymapwindow = Toplevel()

        mapfile = createimagemap()

        tk_im_map = ImageTk.PhotoImage(mapfile)

        global pict_map

        pict_map = Label(modifymapwindow,
                         image = tk_im_map)
        pict_map.pack()

        rotatebutton90 = Button(modifymapwindow,
                                     text="Повернуть текущий тайл на 90 градусов",
                                     font = ("Pixelify Sans",20),
                                    command = tilerotation1,
                                     pady=10,
                                     padx=10
                                     )
        rotatebutton90.pack()

        rotatebutton180 = Button(modifymapwindow,
                                     text="Повернуть текущий тайл на 180 градусов",
                                     font = ("Pixelify Sans",20),
                                     command = tilerotation2,
                                     pady=10,
                                     padx=10)
        rotatebutton180.pack()

        rotatebutton270 = Button(modifymapwindow,
                                    text="Повернуть текущий тайл на 270 градусов",
                                    font = ("Pixelify Sans",20),
                                    command = tilerotation3,
                                    pady=10,
                                    padx=10)
        rotatebutton270.pack()

        rotatebutton360 = Button(modifymapwindow,
                                    text="Повернуть текущий тайл в изначальное положение",
                                    font = ("Pixelify Sans",20),
                                    command = tilerotation4,
                                    pady=10,
                                    padx=10)
        rotatebutton360.pack()

        nexttile = Button(modifymapwindow,
                               text="Изменить другой тайл",
                               font = ("Pixelify Sans",20),
                               command = nexttilebutton,
                               pady=10,
                               padx=10)
        nexttile.pack()

        savemapbutton = Button(modifymapwindow,
                               text="Сохранить карту и завершить работу",
                               font = ("Pixelify Sans",20),
                               command=savemap,
                               pady=10,
                               padx=10)
        savemapbutton.pack()

        modifymapwindow.mainloop()
                
#кнопка выбора тайла
def radiobuttonselector(dictionary, key1, window):
    try:
        global user_choice_tile

        user_choice_tile = IntVar()

        for i in dictionary[key1]:
            icon = PhotoImage(file=dictionary[key1][i])
            tilecode = int(i)
            radiobutton = Radiobutton(window,
                                      text=tilecode,
                                  variable = user_choice_tile,
                                  value=tilecode,
                                  command= lambda t=tilecode: choosetile(t),
                                  image=icon)
            
            radiobutton.pack(anchor=W)
            radiobutton.image = icon
    
    except Exception as e:
        print(e)

    selecttilebutton = Button(window,
                              text = "Выбрать тайл",
                              command=modifymap,
                              font = ("Pixelify Sans",20),
                              state = ACTIVE,
                              compound = 'left')
    selecttilebutton.pack()


def error1(): 
    #диалоговое окно показывающее ошибку
    messagebox.showerror(title="Ошибка!", message="Введите данные в корректном формате")

def error2():
    #диалоговое окно показывающее ошибку
    messagebox.showerror(title="Ошибка!", message="Выберите тайлы и(или) его позицию")

def mapmatrixzeros(size_map):

    #функция создающая матрицу из нулей для карты

    global tiles_x, tiles_y, main_x, main_y, crop_x, crop_y

    main_y = size_map[0]
    main_x = size_map[1]

    tiles_x = ceil(main_x / 16)
    tiles_y = ceil(main_y / 16)
    crop_x = main_x % 16
    crop_y = main_y % 16

    map_matrix = np.zeros((tiles_x, tiles_y), dtype=int)

    return map_matrix

def manualmapcreate(size_map, tiles_dictionary):

    global map_matrix, manualmapwindow2

    map_matrix = mapmatrixzeros(size_map)

    manualmapwindow2 = Tk()
    #новое окно с непосредственно настройкой карты

    manualmapwindow.destroy()
    #матрица с пустыми тайлами

    frame = Frame(manualmapwindow2)
    frame.place(x=0,y=0)
    
    empty_tile = PhotoImage(file='map_assets/empty_tile.png')

    for i in range(tiles_x):
        for j in range(tiles_y):
            global tile_button
            tile_button = Button(text=f"{i} {j}",
                                image=empty_tile)
            tile_button.bind("<Button-1>", lambda event: choosetileonmatrix(event))
            
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
    global namemap
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
            manualmapcreate(size_map,tiles_dictionary)
                

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

