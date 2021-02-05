from tkinter import *
from random import *
import random

main = Tk()
main.title('Jackal v0.1')
main.geometry('1000x1000')

def Game_mode (mode):
    """ Определяет режим игры: один игрок, 1 на 1, 2 на 2,
        3, 4, сетевая игра или против ИИ
    """
    if mode == 'one':
        Creation_pirat(3)

def Field_size (size):
    """ Определяет размер поля: стандарт (11х11), произвольный
        или рандомный
    """
    if size == 'standard':
        Creation_cell(117)
        Creation_coin(37)

def Creation_cell (n):
    """ Создает массив клеток """
    Cells = ['empty1']*10 + ['empty2']*10 + ['empty3']*10 + ['empty4']*10 + ['arrow_one_straight']*3 + \
            ['arrow_one_diagonal']*3 + ['arrow_two_straight']*3 + ['arrow_two_diagonal']*3 + \
            ['arrow_three']*3 + ['arrow_four_straight']*3 + ['arrow_four_diagonal']*3 + ['horse']*2 + \
            ['trap_two']*5 + ['trap_three']*4 + ['trap_four']*2 + ['trap_five']*1 + ['ice']*6 + \
            ['pit']*3 + ['crocodile']*4 + ['cannibal']*1 + ['fortress']*2 + ['resurrection']*1 + \
            ['coin']*5 + ['coins_two']*5 + ['coins_three']*3 + ['coins_four']*2 + ['coins_five']*1 + \
            ['plane']*1 + ['balloon']*2 + ['cannon']*2 + ['rum']*4

    for i in range(n):
        if Cells[i] == 'arrow_one_diagonal':
           Cells[i] += '_' + str(random.randint(1,4))
        elif Cells[i] == 'arrow_one_straight':
            Cells[i] += '_' + str(random.randint(1,4))
        elif Cells[i] == 'arrow_two_diagonal':
            Cells[i] += '_' + str(random.randint(1,2))
        elif Cells[i] == 'arrow_two_straight':
            Cells[i] += '_' + str(random.randint(1,2))
        elif Cells[i] == 'arrow_three':
            Cells[i] += '_' + str(random.randint(1,4))
        elif Cells[i] == 'cannon':
            Cells[i] += '_' + str(random.randint(1,4))
    
    Cells = Random(Cells)
    Reading_pictures (Cells, 13)
    Drawing_cell(13)

def Creation_pirat (n):
    """ Создает массив пиратов """
    Pirats = [0]*n
    for i in range(n):
        Pirats[i] = i
    Drawing_pirat(n)
    Drawing_ship(n/3)

def Creation_coin (n):
    """ Создает массив монеток """
    Coins = [0]*n
    for i in range(n):
        Coins[i] = i

def Creation_button ():
    """ Создает кнопки """
    pass

def Random (data):
    """ Перемешивает массив случайным образом """
    shuffle(data)
    return (data)

def Drawing_cell (n):
    """ Рисует игровое поле """
    global Blocks
    Blocks=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            Blocks[i][j] = Button(main, height=65, width=65,
                                  activebackground = 'white', bg = 'white',
                                  command=lambda x=i, y=j: Click(x, y))
            Blocks[i][j].place(x=10+73*i, y=10+73*j)

    for i in range(n):
        for j in range(n):
            if j!=0 and j!=(n-1) and i!=0 and i!=(n-1):
                Blocks[i][j].config(image = PhotoBack)
            else:
                Blocks[i][j].config(image = PhotoSea)
    Blocks[1][1].config(image = PhotoSea)
    Blocks[1][n-2].config(image = PhotoSea)
    Blocks[n-2][1].config(image = PhotoSea)
    Blocks[n-2][n-2].config(image = PhotoSea)
                                       
def Drawing_pirat (n):
    """ Рисует пиратов на поле """
    global PhotoPirat, Pirats
    PhotoPirat = PhotoImage(file='image/Pirat2.png')

    Pirats = []
    for i in range(n):
        Pirats.append(Button(main, height=20, width=20, image=PhotoPirat,
                             background = 'white', 
                             command=lambda n=n, x=i: Choice_pirat(n, x)))
    
    Pirats[0].place(x=73*6+15, y=15)
    Pirats[1].place(x=73*6+50, y=15)
    Pirats[2].place(x=73*6+15, y=50)

def Drawing_ship (n):
    """ Рисует корабли на поле """
    global PhotoShip
    PhotoShip = PhotoImage(file='image/ship.png')
    Blocks[6][0].config(image = PhotoShip)
    
def Drawing_coin (n):
    """ Рисует монетки на поле """
    pass

def Choice_pirat (n, x):
    """ Срабатывает после нажатие на пирата """
    global id_Pirat, b_x, b_y
    id_Pirat = x
    for i in range(13):
        for j in range(13):
           Blocks[i][j].config(activebackground = 'white', bg = 'white')
    for i in range(n):
        Pirats[i].config(background = 'white')
    Pirats[x].config(background = 'green')
    b_x = int(Pirats[x].place_info()['x'])//73
    b_y = int(Pirats[x].place_info()['y'])//73
    if Blocks[b_x][b_y]['image'] == str(PhotoSea):
        Active_sea(b_x + x, b_y + y)
    else:
        Active_cells(b_x, b_y)  


def Active_cells (x, y):
    """ Активирует клетки """
    if y!=0:
        for i in range(3):
            for j in range(3):
                if Blocks[x+i-1][y+j-1]['image'] != str(PhotoSea):
                    Blocks[x+i-1][y+j-1].config(activebackground = 'blue', bg = 'blue')
    elif x<3: 
        Blocks[x+1][y].config(activebackground = 'blue', bg = 'blue')
        Blocks[x][y+1].config(activebackground = 'blue', bg = 'blue')
    elif x>9: 
        Blocks[x-1][y].config(activebackground = 'blue', bg = 'blue')
        Blocks[x][y+1].config(activebackground = 'blue', bg = 'blue')
    else:
        Blocks[x+1][y].config(activebackground = 'blue', bg = 'blue')
        Blocks[x-1][y].config(activebackground = 'blue', bg = 'blue')
        Blocks[x][y+1].config(activebackground = 'blue', bg = 'blue')

def Reading_pictures (name, n):
    """ Считывает картинки для клеток из папки """
    global PhotoBlocks, PhotoSea, PhotoBack
    PhotoBack = PhotoImage(file='image/0.png')
    PhotoSea = PhotoImage(file='image/sea.png')
    PhotoBlocks = [[0]*n for i in range(n)]
    Photos = []
    for i in range(len(name)):
        Photos.append(PhotoImage(file='image/'+name[i]+'.png'))       
    Photos.append(Photos[0])
    Photos.append(Photos[n-3])
    Photos.append(Photos[(n-2)*(n-3)])
    Photos.append(PhotoSea)
    Photos[0] = Photos[n-3] = Photos[(n-2)*(n-3)] = PhotoSea

    for i in range(n):
        for j in range(n):
            if j!=0 and j!=(n-1) and i!=0 and i!=(n-1):
                PhotoBlocks[i][j]=Photos[(i-1)*(n-2)+(j-1)]
            else:
                PhotoBlocks[i][j]=PhotoSea

def Click(x, y):
    """ Срабатывает при нажатии на клетку """
    if Blocks[x][y]['bg'] == 'white':
        return

    if y==0:
        return (Event_ship(x, y))

    if Blocks[x][y]['image'] == str(PhotoBack):
        Blocks[x][y].config(image = PhotoBlocks[x][y])
    c_x = 73*x + 15 + 35*(id_Pirat % 2)
    c_y = 73*y + 15 + 35*(id_Pirat // 2)
    Pirats[id_Pirat].place(x=c_x, y=c_y)
    Choice_pirat (len(Pirats), id_Pirat)

    if PhotoBlocks[x][y]['file'] == 'image/balloon.png':
        Balloon()
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_straight_1.png':
        Arrow(1, 0)
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_straight_2.png':
        Arrow(0, 1)
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_straight_3.png':
        Arrow(-1, 0)
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_straight_4.png':
        Arrow(0, -1)
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_diagonal_1.png':
        Arrow(1, -1)
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_diagonal_2.png':
        Arrow(1, 1)
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_diagonal_3.png':
        Arrow(-1, 1)
    if PhotoBlocks[x][y]['file'] == 'image/arrow_one_diagonal_4.png':
        Arrow(-1, -1)


def Balloon():
    """ Клетка Воздушный шар """
    for i in range(13):
        if Blocks[i][0]['image'] == str(PhotoShip):
            Event_ship(i,0)

def Arrow(x,y):
    """ Клетка со стрелочкой """
    Click(b_x + x, b_y + y)
    
def Active_sea(x,y):
    """ Попадания пирата в море """
    print('ok')
    
   
def Event_ship(x, y):
    """ Нажатие на корабль """
    c_x = 73*x + 15 + 35*(id_Pirat % 2)
    c_y = 73*y + 15 + 35*(id_Pirat // 2)
    if Blocks[b_x][b_y]['image'] == str(PhotoShip):
        for i in range(len(Pirats)):
            if (int(Pirats[i].place_info()['x'])//73)==b_x and (int(Pirats[i].place_info()['y'])//73)==b_y:
                Pirats[i].place(x=73*x + 15 + 35*(i % 2), y=73*y + 15 + 35*(i // 2))
        Blocks[b_x][b_y].config(image = PhotoSea)
    else:
        Pirats[id_Pirat].place(x=c_x, y=c_y)
    Choice_pirat (len(Pirats), id_Pirat)   
    Blocks[x][y].config(image = PhotoShip)
    

    
Field_size('standard')
Game_mode('one')
main.mainloop()
