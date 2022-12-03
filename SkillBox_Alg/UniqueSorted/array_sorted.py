from typing import List

from printer import print_currency_info, print_phone_info


def group_and_print(phone_numbers: List[int]):
    """Выводит номера телефонов и количество их повторений
    в списке phone_numbers"""
    phone_dict = dict()
    for number in phone_numbers:
        phone_dict[number] = phone_dict.get(number, 0) + 1

    for phone, count in phone_dict.items():
        print_phone_info(phone, count)


def crypto_currency_analysis(file_contents: str):
    """Возвращает среднее значение по группам из строки вида
        "BTC:42
        BTC:600
        BTC:900
        DOGE:123456
        DOGE:69420
        ETH:220
        ETH:666
        XMR:14
        XMR:88"
    """
    print("Input file contents: \n%s" % file_contents)
    currency_dict = {}
    lst = [elem.split(":") for elem in file_contents.split()]
    for key, value in lst:
        currency_dict[key] = currency_dict.get(key, []) + [int(value)]
    for key, values in currency_dict.items():
        print_currency_info(key, (sum(values) / len(values)))


cases = """
        BTC:42
        BTC:600
        BTC:900
        DOGE:123456
        DOGE:69420
        ETH:220
        ETH:666
        XMR:14
        XMR:88
        """
crypto_currency_analysis(cases)