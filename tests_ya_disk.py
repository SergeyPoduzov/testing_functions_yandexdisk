import unittest

from testing_Cheking_yandex_Disk import TOKEN, creating_yandex_disk, cheking_yandex_disk


import requests
import os
import time



class YandexDisktest(unittest.TestCase):
    """тесты для 'name_functions.py'"""

    def setUp(self):
        pass

    def test_creating_dir(self):
        ''' проверяет ли - создан ли каталог и возвращает статтус 201 '''
        creating_yandex_disk_status = creating_yandex_disk('durov21114',TOKEN)
        self.assertEqual(creating_yandex_disk_status, 201)

    def test_existing_dir(self):
        ''' проверяет ли - существует ли такая папка в корне на яндекс диске и возражает dir '''
        time.sleep(1)
        existing_dir_status = cheking_yandex_disk('durov21114', TOKEN)
        self.assertEqual(existing_dir_status, 'dir')


if __name__ == '__main__':
    unittest.main()
