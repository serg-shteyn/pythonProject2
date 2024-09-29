# Игра "крестики - нолики"

def draw_area():
    for i in area:
        print(*i)

def check_winner():
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
        turn_char = "Х "
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

    if check_winner() == "Х":
        print("Победа крестиков")
        break
    if check_winner() == "0":
        print("Победа ноликов")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья")
        break

