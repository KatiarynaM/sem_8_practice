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


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
   
    result = [contact for contact in book if info.lower() in contact.lower()]
    if len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print('Уточните...')
    else:
        print('Ничего не найдено')


def delet_data() -> None:
    """Удаляет результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_delet = input('Введите, что хотите удалить:  ')
    print(contact_to_delet)
    contact_to_delet = search(data, contact_to_delet)
    data.remove(contact_to_delet)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))

def change_data() -> None:
    """Изменяет результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    contact_to_change = input('Введите, что хотите изменить:  ')
    contact_to_change = search(data, contact_to_change)
    print(contact_to_change)
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    data[data.index(contact_to_change)] = f'{fio} | {phone_num}'
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))
