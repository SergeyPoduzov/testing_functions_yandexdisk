import unittest

from testing_home1 import printing_name, printing_shelf, printing_documents, cheking_input_data, adding_document, deleting_adding_document
from testing_home1 import cheking_shelfes, mooving_document, adding_shelf


class NamesTestCase(unittest.TestCase):
    """тесты для 'name_functions.py'"""

    def setUp(self):
        self.documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10006", "name": "Алексей Иванов"},
      ]
        self.directories = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }

    def test_printing_name(self):
        '''"""Выдает имя человека Геннадий Покемонов по документу 11-2"""'''
        output_name = printing_name(self.documents,'11-2')
        self.assertEqual(output_name[0], 'Геннадий Покемонов')

    def test_printing_name2(self):
        '''"""Выдает имя человека Геннадий Покемонов по документу 11-2"""'''
        output_name = printing_name(self.documents, '11-2')
        self.assertIn('Геннадий Покемонов', output_name)

    def test_printing_shelf(self):
        """Выдает номер полки  по документу - документ 10006 будет на полке 2"""
        output_name_shelf = printing_shelf(self.directories, '10006')
        self.assertEqual(output_name_shelf[0], '2')

    def test_printing_documents_list(self):
        """ проверка l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин" """;
        output_documents_list = printing_documents(self.documents)
        self.assertEqual(output_documents_list[0], 'passport "2207 876234" "Василий Гупкин"')

    def test_adding_documents(self):
        '''Проверка что новый документ добавился и он на в списке документов  'type': 'interantional passport', 'number': '1123-1234', 'name': 'Alexander sidorov' '''
        output_adding_documents = adding_document(self.documents, self.directories, '1123-1234', 'interantional passport','Alexander sidorov', '3')
        self.assertIn({'type': 'interantional passport', 'number': '1123-1234', 'name': 'Alexander sidorov'}, output_adding_documents[0])

    def test_adding_documents_shelves(self):
        ''' Проверка что новый добавленный документ появился на второй полке'''
        output_adding_documents = adding_document(self.documents, self.directories, '1123-1234', 'interantional passport','Alexander sidorov', '3')
        self.assertIn('1123-1234',self.directories['3'])

    def test_dell_documents2(self):
        ''' Проверка удаления документа  - удаляем документ 11-2 - он долден удалится из документов'''
        output_delling_documents = deleting_adding_document(self.documents, self.directories, '11-2')
        self.assertNotEqual('11-2',output_delling_documents[0][1]["number"])

    def test_dell_documents3(self):
        ''' Проверка удаления документа  - удаляем документ 11-2 - он долден удалится из полки 1'''
        output_delling_documents = deleting_adding_document(self.documents, self.directories, '11-2')
        self.assertNotIn('11-2', output_delling_documents[1]['1'])

    def test_mooving_documents(self):
        ''' Проверка перемешения  документа 10006 со 2 полки на первую -'''
        output_mooving_document = mooving_document(self.directories, '10006', '1')
        self.assertIn('10006', output_mooving_document['1'])
    def test_adding_shelf(self):
        ''' Проверка добавления новой полки '5'  '''
        output_adding_shelf= adding_shelf(self.directories, '5')
        self.assertEqual([], output_adding_shelf['5'])

    def test_shelf(self):
        ''' Проверка наличия  полки полки '5' после добавления '''
        output_adding_shelf= adding_shelf(self.directories, '5')
        print(cheking_shelfes(self.directories,'5'))
        self.assertTrue(cheking_shelfes(self.directories, '5'))

if __name__ == '__main__':
    unittest.main()
