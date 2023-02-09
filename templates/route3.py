import sys
import requests


api_server = "http://static-maps.yandex.ru/1.x/"

point0 = "37.633219,55.829002"  # Павильон 1
point1 = "37.634567,55.829935"  # Дворец госуслуг МФЦ
point2 = "37.632796,55.831094"  # Павильон 67 Карелия
xod1 = "37.631961,55.830783"
point3 = "37.629093,55.832802"  # Павильон 64 Выставочный комплекс РЖД
xod2 = "37.629093,55.832802"
point4 = "37.628226,55.833238"  # Павильон 59 Зерно
point5 = "37.629994,55.834389"  # Павильон Макет Москвы
point6 = "37.626836,55.836105"  # Арт-резиденция и мастерские музея Гараж
point7 = "37.623396,55.835053"  # Музей оптических иллюзий
point8 = "37.620542,55.836631"  # Музей Гаража особого назначения ФСО России
point9 = "37.618426,55.837991"  # Выход к набережной

coordinates = [point0, point1, point2, xod1, point3, xod2,
               point4, point5, point6, point7, point8, point9]
dots = ["37.633219,55.829002,pm2al", "37.634567,55.829935,pm2lbl1", "37.632796,55.831094,pm2lbl2",
        "37.629093,55.832802,pm2lbl3", "37.628226,55.833238,pm2lbl4", "37.629994,55.834389,pm2lbl5",
        "37.626836,55.836105,pm2lbl6", "37.623396,55.835053,pm2lbl7", "37.620542,55.836631,pm2lbl8",
        "37.618426,55.837991,pm2bl"]


params = {
    "ll": "37.624178" + "," + "55.833572",
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
map_file = "map3.png"
with open(map_file, "wb") as file:
    file.write(response.content)