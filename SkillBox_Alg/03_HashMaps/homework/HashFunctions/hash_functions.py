class Student:
    age: int
    name: str

    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name


def hash_string(value: str) -> int:
    """возвращает сумму кодов всимволов в строке"""
    from functools import reduce
    result = reduce(lambda tot, elem: tot + ord(elem), value, 0)
    return result

def hash_int(value: int) -> int:
    """возвращает произведение цифр числа value, наличие ноля обнуляет результат"""
    result = 1
    while value > 0:
        result *= value % 10
        value //= 10
    return result

def hash_student(value: Student) -> int:
    """возвращает сумму хэшей атрибутов экземпляра класса Student"""
    result = hash_int(value.age) + hash_string(value.name)
    return result

stud1 = Student(54, "Nike")
print(hash_student(stud1))