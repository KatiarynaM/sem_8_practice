def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))

#or
''' lines = book.splitlines()
    res = []
    for line in lines:
        if info in line:
            res.append(line)
    return res'''

#or
#book = book.split('\n')
#  return [contact for contact in book if info.lower() in contact.lower()]
 

def delet_data() -> None:
    """Удаляет результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите удалить:  ')
    result = search(data, contact_to_find)
    print(result)
    if len(result) == 1:
        result.write()
    elif len(result) > 1:
        print('Уточните...')
    else:
        print('Ничего не найдено')
    
def change_data() -> None:
    """Изменяет результат поиска по справочнику."""
    with open('book.txt', 'r+', encoding='utf-8') as file:
    data = file.read()
    contact_to_find = input('Введите, что хотите изменить:  ')
    result = search(data, contact_to_find)
    print(result)
    if len(result) == 1:
        fio = input('Измените ФИО: ')
        phone_num = input('Измените номер телефона: ')
        with open('book.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{fio} | {phone_num}')
    elif len(result) > 1:
        print('Уточните...')
    else:
        print('Ничего не найдено')
