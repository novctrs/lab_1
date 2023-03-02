# Math quadratic equations

import math
def quad_eq(a,b,c):
    dis=(b**2)-(4*a*c)
    if dis<0:
        print('equation has no solutions')
    elif dis==0:
        sol=(-b)/(2*a)
        print('x=',sol)
    elif dis>0:
        sol1=((-b)+math.sqrt(dis))/(2*a)
        sol2 = ((-b) - math.sqrt(dis)) / (2 * a)
        print('x=',sol1,'x=',sol2)

quad_eq(1,2,3)

# area of a circle

from math import pi

def c_area(r):
    area=pi*(r**2)

circle=c_area(3)
print(circle)

# counter

import random
from collections import Counter

def random_list(length=100, rnge=10):
    arr=[]
    for i in range(length):
        arr.append(random.randint(0, rnge))
    return arr

def find_number(arr,number=1):
    count=[]
    for key, value in Counter(arr).items():
        if value == number:
            count.append(key)
    print(count)

array = random_list(100,20)
number_count = find_number(array, 4)
print(number_count)

# the most frequent number

import random
from collections import Counter

def random_list(length=100, rnge=10):
    arr=[]
    for i in range(length):
        arr.append(random.randint(0, rnge))
    return arr

def max (lst):
    counter = Counter(a)
    result = a[0]
    max_count = counter[result]
    for number, count in counter.items():
        if count > max_count or (count == max_count and number > result):
            result = number
            max_count = count
    return result, max_count

a = random_list()
num, m_count = max (a)
print(f'the most frequent number: {num}, count: {m_count}')

# code_words_atom_nebo

import itertools

def words_no_rep (word ,length,letter=''):
    k = 0
    a = list(itertools.product(word, repeat = length))
    if letter=='':
        k=len(a)
    else:
        for x in a:
            if x.count(letter) == 1:
                k += 1
    return k

atom =words_no_rep('atom',5,'m')
print(atom)
nebo = words_no_rep('nebo',6)
print(nebo)

# cycle

from itertools import cycle

def infinite(lst, tries):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(tries):
            result += str(next(iter_lst))
    return result

print(infinite([2, 5, 8], 7))
print(infinite([], 1000))
print(infinite([7], 4))

# json
# С помощью json модуля напишите скрипт, который считывает файл JSON,
# содержащий информацию о книгах (название, авторов, ISBN, количество страниц,
# статус публикации, тематику и т.д.), и выводит список всех книг,
# в которых количество страниц больше 500.
# (Файл books.json)

import json

def length_books(data, pagecount):
    books=[]
    for i in data:
        if i.get('pageCount')>pagecount:
            books.append(i['title'])
    return (books)

with open('books.json') as f:
    book = json.load(f)
long_books = length_books(book,500)
print(f'there are {len(long_books)} long books in this catalogue:')
for i in long_books:
    print(i)

# csv_1 (BMI)

import csv

def find_people(people,a='M'):
    ppl_list=[]
    for i in people:
        a= i.get("Sex")
        b=int(i.get(' "Weight (Sep)"'))
        c=int(i.get(' "Weight (Apr)"'))
        d=float(i.get(' "BMI (Apr)"'))
        if a=='M' and b-c<0 and d>20:
            ppl_list.append(i)
    return ppl_list

with open('freshman_kgs.csv', 'r') as f:
    reader = csv.DictReader(f)
    people_list = list(reader)

men_list=find_people(people_list)

# csv_2 homes
# 2. Файл homes.csv, где представлена статистика по продаже домов.
# Столбцы: цена продажи и запрашиваемая цена (в тыс.долларов), жилая площадь,
# количество комнат, ванных комнат, возраст дома, количество акров на участке, налог (в долларах).
# Нужно рассчитать среднюю итоговую стоимость дома с восемью комнатами,
# а также создать новый столбец, в котором были бы только дома со стоимостью более 180 и налогом менее 3500.

import csv

def avg_price(homes_list, rooms):
    room = []
    total = 0
    for i in homes_list:
        a = i.get(' "Rooms"')
        if type(a) == str and int(a) == rooms:
            room.append(i)
            b = int(i.get('Sell'))
            total += b
    avg_sell = round(total / len(room))
    return avg_sell, room

def exp_tax(homes_list,price=180, tax=3500):
    for i in homes_list[:-1]:
        c=i.get("Sell")
        d=i.get(' "Taxes"')
        if int(c)>price and int(d)<tax:
            i[f'Sell>{price} & Taxes <{tax}']=True
        else:
            i[f'Sell>{price} & Taxes <{tax}'] = False
    return homes_list

def create_df(homes_list):
    csv_columns = list(homes_list[1].keys())
    csv_file = "homes2.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in homes_list:
            writer.writerow(data)

with open('homes.csv', 'r+') as f:
    reader = csv.DictReader(f)
    home_list = list(reader)

price, eight_rooms = avg_price(home_list,8)
print(price)

exp_list = exp_tax(home_list)
create_df(exp_list)

