import sys
import requests


def create_map(file_name, center='37.633219,55.829002', spn='0.005,0.005', l='map'):
    map_req = "http://static-maps.yandex.ru/1.x/"
    file = open(file_name).readlines()
    file = list(map(lambda x: x.split(' ')[0], file))

    params = {
        "ll": center,
        "l": l,
        "spn": spn,
        "pl": ','.join(file)
    }

    response = requests.get(map_req, params=params)

    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    clear_file_name = file_name.split('/')[1]
    new_file_name = clear_file_name.split('.')[0]
    map_file = "static/" + new_file_name + ".png"
    with open(map_file, "wb") as file:
        file.write(response.content)
        file.close()