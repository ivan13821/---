import random

blocks = 4
def pretty_print(mas):
    print('-'*10)
    for row in mas:
        print(*row)
    print('-' * 10)

def get_number_from_index(i, j):
    return i*blocks + j + 1

def get_empty_list(mas):
    empty = []
    for i in range(blocks):
        for j in range(blocks):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty

def get_index_from_number(num):
    num -= 1
    x, y = num//blocks, num%blocks
    return x, y

def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas

def is_zero_in_mas(mas):
    zero = 0
    for i in mas:
        if 0 in i:
            return True

    return False

def move_left(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for row in range(4):
        for col in range(3):
            if mas[row][col] == mas[row][col+1] and mas[row][col] != 0:
                mas[row][col] *= 2
                mas[row].pop(col + 1)
                mas[row].append(0)
    return mas

def move_right(mas):
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for row in range(4):
        for col in range(3, 0, -1):
            if mas[row][col] == mas[row][col - 1] and mas[row][col] != 0:
                mas[row][col] *= 2
                mas[row].pop(col - 1)
                mas[row].insert(0, 0)
    return mas

def move_up(mas):
    for j in range(4):
        res = []
        for i in range(4):
            if mas[i][j] != 0:
                res.append(mas[i][j])
        while len(res) != 4:
            res.append(0)
        for i in range(3):
            if res[i] == res[i+1]:
                res[i] *= 2
                res.pop(i+1)
                res.append(0)
        for i in range(4):
            mas[i][j] = res[i]
    return mas

def move_down(mas):
    for j in range(4):
        res = []
        for i in range(4):
            if mas[i][j] != 0:
                res.append(mas[i][j])
        while len(res) != 4:
            res.insert(0, 0)
        for i in range(3, 0, -1):
            if res[i] == res[i-1]:
                res[i] *= 2
                res.pop(i-1)
                res.insert(0, 0)
        for i in range(4):
            mas[i][j] = res[i]
    return mas

def can_move(mas):
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas [i][j+1] or mas[i][j] == mas[i+1][j]:
                return True
    return False

def score(mas):
    res = 0
    for i in range(4):
        for j in range(4):
            res += mas[i][j]
    return res












