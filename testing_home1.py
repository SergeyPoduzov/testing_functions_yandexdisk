# Сергей Подузов, 36 группа. sergey.poduzov@gmail.com
# Занятие  5. Задача 2.

# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень
# внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
#
#       documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
#       ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
#
#       directories = {
#         '1': ['2207 876234', '11-2'],
#         '2': ['10006'],
#         '3': []
#       }
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека,
# которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки,
# на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234"
# "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его
# номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте
# ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций.
# Функции должны иметь выразительное название, передающие её действие.
# d – delete – команда, которая спросит номер документа и удалит его из
# каталога и из перечня полок. Предусмотрите сценарий, когда пользователь
# вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и
# переместит его с текущей полки на целевую. Корректно обработайте кейсы,
# когда пользователь пытается переместить несуществующий документ или
# переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее
# в перечень. Предусмотрите случай, когда пользователь добавляет полку,
# которая уже существует.;

#
# Каталог документов хранится в следующем виде:
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10006", "name": "Алексей Иванов"},
      ]
# Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


# p – people – команда, которая спросит номер документа и выведет имя человека,
# которому он принадлежит;
def printing_name(documents, document_number):
    """Выдает имя человека по документу"""

    names=[]
    for document in documents:
        if document["number"]==document_number:
            names.append(document["name"])
    return names

def printing_shelf(directories, document_number):
    """Выдает номер полки  по документу"""
    # s – shelf – команда, которая спросит номер документа и выведет номер полки,
    # на которой он находится;
    shelves=[]
    for key, value in directories.items():
        if document_number in value:
            shelves.append(key)
    return shelves

def printing_documents(documents):
    """ l– list – команда, которая выведет список всех документов в формате
    passport "2207 876234" "Василий Гупкин";"""

    if documents:
        new_documents_for_printing = []
        # print("\nСписок всех документов:")
        for document in documents:
            doc=''
            output_documents=[]
            for value in document.values():

                output_documents.append(value)
            doc = f'{output_documents[0]} "{output_documents[1]}" "{output_documents[2]}"'
            new_documents_for_printing.append(doc)
        return new_documents_for_printing


def cheking_input_data(input_data):
    """Функуия которая форматирует ввод номер документа или команды, убирает пробелы внутри и слеви спрва"""

    # document_number=''.join(document_number)
    # Убираем проблемы слева и спрва
    # приводим к нижнему регистру
    input_data=input_data.strip()
    input_data = input_data.lower()
    return input_data

def adding_document(documents, directories, number, type, name, shelf):
    '''# a – add – команда, которая добавит новый документ в каталог и в перечень полок,
#спросив его  номер, тип, имя владельца и номер полки, на котором он будет
# храниться. Корректно обработайте
# ситуацию, когда пользователь будет пытаться добавить документ на
 несуществующую полку.
'''
    # Проверка не существующей полки
    if int(shelf) > len(directories):
        return


    else:


        dict1={}
        dict_return =[]
        dict1["type"]=type
        dict1["number"] = number
        dict1["name"] = name
        documents.append(dict1)

        for key, value in directories.items():
            if key == shelf:
                directories[key].append(number)

        dict_return = [documents, directories]
        return dict_return


# d – delete – команда, которая спросит номер документа и удалит его из
# каталога и из перечня полок. Предусмотрите сценарий, когда пользователь
# вводит несуществующий документ;


# def deleting_adding_document(documents,directories, document_number):
def deleting_adding_document(documents, directories, document_number):
    #в начале найдем и дувлим из documents
    # Удаление ключа: del alien_0['x_position']
    # ●.remove(el) удаляет указанный элемент из списка;

    #Вначале проверка на существуещт документ или нет в списке
    del_doc1 = []
    for doc in documents:
        if doc['number'] == document_number:
            del_doc1.append(document_number)

    # Если такой доумент есть в списке, то идем его удалять, если нет, то пишет что нет такоо документа
    if del_doc1:

        del_doc = []
        stroka = []
        for doc in documents:
            for value in doc.values():
                if value == document_number:
                    del_doc.append(value)
                    stroka.append(doc)
        if stroka:
            for elem in stroka:
                documents.remove(elem)

        # Если докумен есть в таблице documents, тогда мы его удалем из полок,
        if del_doc:
            # Будм запоминать ключи, которые надо удалить
            keys = []
            for key, value in directories.items():
                if document_number in value:
                    keys.append(key)
            for key in keys:
                directories[key] = []

        dict_return = [documents, directories]
        return dict_return


    else:
        print("пользователь  вводит несуществующий документ")
        return




    del_doc=[]
    stroka=[]
    for doc in documents:
        for value in doc.values():
            if value==document_number:
                del_doc.append(value)
                stroka.append(doc)
    if stroka:
        for elem in stroka:
            documents.remove(elem)

    #Если докумен есть в таблице documents, тогда мы его удалем из полок,
    if del_doc:
        #Будм запоминать ключи, которые надо удалить
        keys=[]
        for key, value in directories.items():
            if document_number in value:
                keys.append(key)
        for key in keys:
            directories[key]=[]


    #Делаем новый выходной список, в который выложим обновленный documents,directories и удаленные номера del_doc

    return del_doc

def cheking_documents(docs):
    """Функция наличия документа. Выдает True/False"""
    docs_cheking=False
    for document in documents:
        for value in document.values():
            if value==docs:
                docs_cheking = True
    return docs_cheking

def cheking_shelfes(directories, chelf):
    """Функция налия полки Выдает True/False"""
    shelf_cheking=False
    for key in directories.keys():
        if key==chelf:
            shelf_cheking = True
    return shelf_cheking


# m – move – команда, которая спросит номер документа и целевую полку и
# переместит его с текущей полки на целевую. Корректно обработайте кейсы,
# когда пользователь пытается переместить несуществующий документ или
# переместить документ на несуществующую полку;

def mooving_document(directories, docs, shelf):
    """Вначале удалим документ с полки, потом добавим."""
    #удаление документа

    for key, value in directories.items():
        for elem in value:
            if elem==docs:
                value.remove(elem)

    #добавление документа на полку
    a = directories[shelf]
    a.append(docs)
    directories[shelf]=a

    return directories

# as – add shelf – команда, которая спросит номер новой полки и добавит ее
# в перечень. Предусмотрите случай, когда пользователь добавляет полку,
# которая уже существует.;

def adding_shelf(directories, shelf_number):
    # Если введут уже существующую полку
    if cheking_shelfes(directories, shelf_number) == True:
        return
    else:


        directories[shelf_number] = []
        return directories




def main():
    print("""Введите команды: 
p – people – команда, которая спросит номер документа и выведет имя человека, 
которому он принадлежит;
s – shelf – команда, которая спросит номер документа и выведет номер полки,
на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
l– list – команда, которая выведет список всех документов в формате passport "2207 876234"
"Василий Гупкин";
a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его
номер, тип, имя владельца и номер полки, на котором он будет храниться. 
quit - выход из программы
d – delete – команда, которая спросит номер документа и удалит его из
каталога и из перечня полок. Предусмотрите сценарий, когда пользователь
вводит несуществующий документ;
m – move – команда, которая спросит номер документа и целевую полку и 
переместит его с текущей полки на целевую. Корректно обработайте кейсы, 
когда пользователь пытается переместить несуществующий документ или переместить 
документ на несуществующую полку;
as – add shelf – команда, которая спросит номер новой полки и добавит ее в 
перечень. Предусмотрите случай, когда пользователь добавляет полку, которая 
уже существует.;
Дополнительные технические функции:
print - выводит documents
shelfs - выводит directories
""")



    active=True
    while active:

        prompt1 = "\nВведите команду или quit для выхода из программы:"
        comand = input(prompt1)
        comand=cheking_input_data(comand)

        # p – people – команда, которая спросит номер документа и выведет имя человека,
        # которому он принадлежит;
        if comand == 'p' or comand=='people':
            active2=True
            while active2:

                prompt2 = "Введите документ:"
                document_number = input(prompt2)
                document_number = cheking_input_data(document_number)
                if document_number=='quit':
                    break
                names = printing_name(documents, document_number)

                if names:
                    for name in names:
                        print("Имя человека с этим документом: " + name)
                    break
                else:
                    print("пользователь  вводит несуществующий документ")

        # s – shelf – команда, которая спросит номер документа и выведет номер полки,
        # на которой он находится;
        elif comand == 's' or comand=='shelf':
            active2 = True
            while active2:
                prompt2 = "Введите документ или quit чтобы вернутся обратно:"
                document_number = input(prompt2)
                document_number = cheking_input_data(document_number)
                if document_number == 'quit':
                    break
                shelves = printing_shelf(directories, document_number)
                if shelves:
                    for shelve in shelves:
                        print("Номер полки с этим документом: " + shelve)
                    break
                else:
                    print("пользователь  вводит несуществующий документ")

        # l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
        elif comand == 'l' or comand=='list':
            doc = printing_documents(documents)
            if doc:
                for docs in doc:
                    print(docs)
            else:
                print('список документов пуст')

        # a – add – команда, которая добавит новый документ в каталог и в перечень полок,
        #спросив его  номер, тип, имя владельца и номер полки, на котором он будет
        # храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
        elif comand == 'a' or comand=='add':


            print("\nВведите номер документа, тип, имя владельца и номер полки.")

            number = input("Введите номер документа: ")
            type = input("Введите тип документа: ")
            name = input("Ведите Имя и Фамилию: ")

            # Ввод и проверка существуте номер полки или нет
            active1 = True
            while active1:
                shelf = input("Введите номер полки (цифрой) :")
                shelf = cheking_input_data(shelf)
                if int(shelf) > len(directories):
                    print("\Вы ввели не существующий номер полки")
                    continue
                else:
                    break

            adding_document(documents, directories, number, type, name, shelf)
            print(f'Документ {type} с номером {number} на имя {name} на полку {shelf} добавлен')
            print('\tДокументы: ')
            for doc in documents:
                print(doc)
            print('\tПолки: ')
            for dir in directories:
                print (directories[dir])



        elif comand == 'print':
            for doc in documents:
                print(doc)

        elif comand == 'shelfs':
            for key, value in directories.items():
                print(str(key)+ ":"+str(value))

        elif comand == 'd' or comand=='delete':


        # d – delete – команда, которая спросит номер документа и удалит его из
        # каталога и из перечня полок. Предусмотрите сценарий, когда пользователь
        # вводит несуществующий документ;
            active2 = True
            while active2:
                prompt2 = "Введите документ или quit чтобы вернутся обратно:"
                document_number = input(prompt2)
                document_number = cheking_input_data(document_number)
                if document_number == 'quit':
                    break

                del_doc=[]
                for doc in documents:
                    if doc['number'] == document_number:
                        del_doc.append(document_number)

                # Если такой доумент есть в списке, то идем его удалять, если нет, то пишет что нет такоо документа
                if del_doc:
                    deleting_adding_document(documents, directories, document_number)
                    print(f'Документ { document_number} удален!')
                    break
                else:
                    print("пользователь  вводит несуществующий документ")
                    continue




        elif comand == 'm' or comand == 'move':
            active2 = True
            active3 = True
            s1=False
            s2=False
            shelf_number=[]
            document_number=[]
            while active2:
                prompt2 = "Введите документ или quit чтобы вернутся обратно:"
                document_number = input(prompt2)
                document_number = cheking_input_data(document_number)
                if document_number == 'quit':
                    break
                #проверяем наличие документа
                elif cheking_documents(document_number)==False:
                    print("Вы ввели несуществующий документ")
                    continue

                else:
                    s1=True

                while active3:
                    #ввод целевой полки
                    prompt3 = "Введите целевую полку, куда положить документ, или quit чтобы вернутся обратно:"
                    shelf_number = input(prompt3)
                    shelf_number = cheking_input_data(shelf_number)
                    if shelf_number == 'quit':
                        break
                    # проверяем наличие полки
                    elif cheking_shelfes(directories, shelf_number)==False:
                        print("Вы ввели несуществующую полку")
                        continue
                    else:
                        s2=True
                        break


                if (s1==True) and (s2==True):
                    mooving_document(directories, document_number, shelf_number)
                    print(f'Документ с номером {document_number} перемещен на полку {shelf_number}')
                    break
                break

        elif comand == 'as' or comand == 'add shelf':
            active2 = True
            s1=False
            shelf_number=[]
            while active2:
                # ввод целевой полки
                prompt3 = "Введите номер  новой полки или нажмите quit чтобы вернутся на уровень выше: "
                shelf_number = input(prompt3)
                shelf_number = cheking_input_data(shelf_number)
                if shelf_number == 'quit':
                    break
                # проверяем наличие полки
                elif cheking_shelfes(directories, shelf_number) == True:
                    print("Вы ввели уже существующую полку")
                    continue
                else:
                    s1=True
                    break
            if s1==True:
                adding_shelf(directories, shelf_number)
                print(f'Вы добавили новую полку {shelf_number}')





        elif  comand == 'quit':
            print("Досвидания!")

            break


if __name__ == '__main__':
    main()