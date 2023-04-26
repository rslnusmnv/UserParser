import pandas as pd
import json
from datetime import datetime

# загружаем таблицу в объект DataFrame
df = pd.read_csv('testaccounts.csv', header=None)

# запрашиваем у пользователя значения start_row и end_row
while True:
    start_row = input('Введите номер начальной строки: ')
    end_row = input('Введите номер конечной строки: ')

    # проверяем корректность введенных значений
    if start_row.isdigit() and end_row.isdigit() and int(start_row) <= int(end_row) <= len(df):
        start_row = int(start_row)
        end_row = int(end_row)
        break
    else:
        print('Ошибка! Проверьте корректность введенных значений.')


# создаем пустой список для хранения JSON-объектов
json_list = []

# проходимся по всем строкам таблицы
for i in range(start_row-1, end_row):
    # создаем пустой словарь для текущей строки
    json_dict = {}

    # выбираем значения столбцов по их индексам
    json_dict['firstName'] = df.iloc[i, 7]
    json_dict['lastName'] = df.iloc[i, 5]
    json_dict['reservationNumber'] = df.iloc[i, 17]

    # разбираем строку даты в объект datetime
    try:
        date_obj = datetime.strptime(df.iloc[i, 14], '%d-%b-%y')
    except ValueError:
        date_obj = datetime.strptime(df.iloc[i, 14], '%d%b%Y')

    # преобразуем объект datetime в строку в нужном формате
    date_formatted = date_obj.strftime('%Y-%m-%d')

    json_dict['birthDate'] = date_formatted

    # добавляем JSON-объект в список
    json_list.append(json_dict)

# преобразуем список JSON-объектов в строку JSON
json_str = json.dumps(json_list)

# выводим полученную строку JSON
with open('output.json', 'w') as file:
    file.write(json_str)
