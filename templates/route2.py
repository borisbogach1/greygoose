import sys
import requests

map_req = "http://static-maps.yandex.ru/1.x/"

p_1 = '37.633219,55.829002'  # Павильон 1
p_2 = '37.632717,55.828590'  # дорога
p_3 = '37.632074,55.828973'  # поворот
p_4 = '37.631369,55.828974'  # Павильон
p_5 = '37.630791,55.828941'  # поворот
p_6 = '37.630390,55.829128'  # дорога
p_7 = '37.629805,55.828823'  # Павильон 5
p_8 = '37.629410,55.829131'  #  дорога
p_8_1 = '37.629449,55.829160'  # Павильон 6
p_9 = '37.629784,55.829377'  # дорога
p_10 = '37.629225,55.829422'  # поворот
p_11 = '37.628445,55.828983'  # дорога
p_12 = '37.628187,55.829173'  # Павильон9
p_13 = '37.627749,55.828605'  # дорога
p_14 = '37.627448,55.828821'  # Павильон 8
p_15 = '37.628058,55.828491'  # в парк
p_16 = '37.627903,55.828415'  # поворот
p_17 = '37.628197,55.828242'  # ещё поворот
p_18 = '37.627939,55.828121'  # кафэ конец


coordinats = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_11, p_13, p_14, p_13, p_15, p_16, p_17, p_18]
points = ['37.633219,55.829002,pm2ntm1', '37.631369,55.828974,pm2dbm2',
          '37.629805,55.828823,pm2blm3', '37.629449,55.829160,pm2wtm4',
          '37.628187,55.829173,pm2ywm5', '37.627448,55.828821,pm2orm6']

params = {
    "ll": '37.630560,55.829250',
    "spn": '0.005,0.005',
    "l": 'map',
    "pl": ','.join(coordinats),
    "pt": '~'.join(points)
}

response = requests.get(map_req, params=params)


if not response:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map2.png"
with open(map_file, "wb") as file:
    file.write(response.content)