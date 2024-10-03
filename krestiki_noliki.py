    # Игра "крестики - нолики"

def draw_area():
    for i in area:
        print(*i)

def check_winner(x=[]):
    x.append([area[0][0],area[0][1],area[0][2]])
    x.append([area[1][0],area[1][1],area[1][2]])
    x.append([area[2][0],area[2][1],area[2][2]])
    x.append([area[0][0],area[1][0],area[2][0]])
    x.append([area[0][1],area[1][1],area[2][1]])
    x.append([area[0][2],area[1][2],area[2][2]])
    x.append([area[0][0],area[1][1],area[2][2]])
    x.append([area[0][2],area[1][1],area[2][0]])
    for i in x:
        if i[0]==i[1] and i[1]==i[2]:
            if "0" in i[0]:
                return "0"
            elif "X" in i[0]:
                return "X"
    else:
        return "*"


area = [['* ','* ','* '],['* ','* ','* '],['* ','* ','* ']]
print("Добро пожаловать в крестики нолики!")
print("-" * 35)
draw_area()
for turn in range(1,10):
    print(f"Ход {turn}: ")
    if turn % 2 == 0:
        turn_char = "0 "
        print("Ходят нолики")
    else:
        turn_char = "X "
        print("Ходят крестики")
    row = int(input("Введите номер строки от 1 до 3: "))-1
    column = int(input("Введите номер столбца от 1 до 3: "))-1
    if area[row][column] == '* ':
        area[row][column] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход!")
        draw_area()
        continue
    draw_area()
    if check_winner() == "0":
        print ("Победа ноликов !!!")
        break
    if check_winner() == "X":
        print ("Победа крестиков !!!")
        break
    if check_winner() == "*" and turn == 9:
        print ("Ничья !!!")
        break
    
    

