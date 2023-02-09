import sys
import requests


api_server = "http://static-maps.yandex.ru/1.x/"

point0 = "37.633219,55.829002"  # Павильон 1
point1 = "37.629612,55.828740"  # Робостанция
point2 = "37.631089,55.829551"  # Каток ВДНХ (фонтан дружбы народов)
xod1 = "37.631336,55.83023"
xod2 = "37.629292,55.831449"
point3 = "37.627297,55.831111"  # Павильон 14 Азербайджан
xod3 = "37.626968,55.831988"
point4 = "37.627115,55.832767"  # Центр славянской письменности
point5 = "37.623396,55.835053"  # Музей оптических иллюзий
xod4 = "37.622037,55.834083"
point6 = "37.619690,55.833714"  # Музей нефти
point7 = "37.618900,55.832966"  # Москвариум
point8 = "37.619018,55.831350"  # Кафе Оттепель
point9 = "37.617955,55.830233"  # Вход в парк, чтобы свалить с ВДНХ

coordinates = [point0, point1, point2, xod1, xod2, point3, xod3,
               point4, point5, xod4, point6, point7, point8, point9]
dots = ["37.633219,55.829002,pm2al", "37.629612,55.828740,pm2lbl1", "37.631812,55.829851,pm2lbl2",
        "37.627297,55.831111,pm2lbl3", "37.627115,55.832767,pm2lbl4", "37.623396,55.835053,pm2lbl5",
        "37.619690,55.833714,pm2lbl6", "37.618900,55.832966,pm2lbl7", "37.619018,55.831350,pm2dol8",
        "37.617955,55.830233,pm2bl"]

params = {
    "ll": "37.628028" + "," + "55.832163",
    "spn": "0.006" + "," + "0.006",
    "l": "map",
    "pl": ','.join(coordinates),
    "pt": '~'.join(dots)
}

response = requests.get(api_server, params=params)

if not response:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map4.png"
with open(map_file, "wb") as file:
    file.write(response.content)