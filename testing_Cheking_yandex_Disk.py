TOKEN=''


import requests
import os

HEADERS = {"Authorization":f"OAuth {TOKEN}"}

def getting_name_dir():
    """Вводим имя новой папке на Яндекс диске"""
    active1 = True
    while active1:
        new_yandex_dir = input(
            "Ведите имя нового каталога в Яндекс диск: ")
        new_yandex_dir = new_yandex_dir.strip()
        new_yandex_dir = new_yandex_dir.split(' ')

        if (len(new_yandex_dir) > 1 or  len(new_yandex_dir[0]) ==0):
            print('Вы ввели имя с ошибкой, повторите')
            continue
        else:
            return new_yandex_dir[0]

def cheking_yandex_disk(dir_name, TOKEN):
    """Функцйия проверки имени файла или каталога"""
    response = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources",
        params={
            "path": dir_name,  # Запись c именем GET/v1/disk/resources

        },
        headers={"Authorization":f"OAuth {TOKEN}"}
    )
    # print("status: ", response.raise_for_status())

    # Выдаете или dir или file
    type = response.json()['type']
    return type

def creating_yandex_disk(new_dir, TOKEN):
    """Функция создания каталога нового"""
    response = requests.put(
            "https://cloud-api.yandex.net/v1/disk/resources",
            params={
                "path": new_dir,  # Запись c именем

            },
            headers={"Authorization":f"OAuth {TOKEN}"}
        )

    answer= response.status_code

    return answer

def getting_list_files(TOKEN):

    response = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/files",
        params={
            # "path": new_dir,  # Запись c именем

        },
        headers={"Authorization":f"OAuth {TOKEN}"}
    )

    answer1 = response.raise_for_status()
    print(answer1)
    answer2  = response.json()
    print(answer2)
    # return answer

def getting_info_disk():
    """Получение мета-информации о диске"""
    response = requests.get(
        "https://cloud-api.yandex.net/v1/disk/",
        params={
            # "path": new_dir,  # Запись c именем

        },
        headers=HEADERS
    )

    answer1 = response.raise_for_status()
    print(answer1)
    answer2  = response.json()
    print(answer2)

def getting_publik_info(TOKEN):
    """Получение данных о опубликованных ресурсах"""
    response = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/public",
        params={
            "type": 'dir',
            'limit': 100,

        },
        headers={"Authorization":f"OAuth {TOKEN}"}
    )

    answer1 = response.raise_for_status()
    print(answer1)
    answer2  = response.json()
    print(answer2)
# https://cloud-api.yandex.net/v1/disk/resources/public

def main():

    print("Создание каталога на Яндекс Диске")

    #Ввод нового папки на яндекс диске
    new_dir = getting_name_dir()

    # проверка статуса
    try:
        type = cheking_yandex_disk(new_dir, TOKEN)
        if type == 'dir':
            print(f'Такой каталог с именем {new_dir} существует')
        elif type == 'file':
            print(f'Такой файл с именем {new_dir} существует')

    except:
        print(f"Такого файла или каталога {new_dir} не существует и будет создан")
        print(f"Создаем новый диск с именем {new_dir}...")
        creating_yandex_disk(new_dir, TOKEN)
        print("Новый каталог создан!")

        # Проверка того что новый каталог был создан:
        print(f"Проверим с новый каталог с именем {new_dir} существует на Яндекс Диске")
        type = cheking_yandex_disk(new_dir, TOKEN)
        if type == 'dir':
            print(f'Такой каталог с именем {new_dir} существует')
        elif type == 'file':
            print(f'Такой файл с именем {new_dir} существует!')




if __name__ == '__main__':
    main()