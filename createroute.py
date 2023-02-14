import sys
import requests
import os
import shutil

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
        # sys.exit(1)
    map_file = "/static/"+file_name[:2]+"png"
    with open(map_file, "wb") as file:
        file.write(response.content)
        file.close()


    # os.rename(map_file, "/static")
    # os.replace(map_file, "/static")
    # shutil.move(map_file, "/static")
