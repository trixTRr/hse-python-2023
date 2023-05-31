from typing import Iterable
import random
import re

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    # пиши код здесь
    greeting = "Привет, " + name + "!"
    return greeting


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    # пиши код здесь
    amount = round(random.uniform(100, 1000000), 2)
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    # пиши код здесь
    pattern = r'^\+7\d{10}$'  # регулярное выражение для проверки формата номера телефона
    match = re.search(pattern, phone_number)
    if match:
        return True
    else:
        return False
    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    # пиши код здесь
    try:
        transfer_amount = float(transfer_amount)  # преобразуем строку в число с плавающей точкой
    except ValueError:
        return False  # если преобразование не удалось, возвращаем False

    if current_amount >= transfer_amount:
        return True
    else:
        return False


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """

    # пиши код здесь
    # удаляем лишние пробелы
    text = ' '.join(text.split())

    # удаляем опасные символы
    text = text.replace('"', '').replace("'", '')

    # заменяем слова на #
    for word in uncultured_words:
        text = text.replace(word, '#' * len(word))

    # делаем первую букву заглавной, а остальные - строчными
    text = text.capitalize()

    return text


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:

    Иванов,Петр,Сергеевич,01.01.1991,10000

    Что должны вернуть на ее основе:

    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000

    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    # пиши код здесь
    # Разделение строки на части по запятым
    parts = user_info.split(",")
    # Формирование текста заявки с использованием отформатированных строк
    result = f"Фамилия: {parts[0]}\nИмя: {parts[1]}\nОтчество: {parts[2]}\nДата рождения: {parts[3]}\nЗапрошенная сумма: {parts[4]}"
    return result