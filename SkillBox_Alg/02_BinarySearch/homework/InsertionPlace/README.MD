# ДЗ

### 1. Новояз
★★☆☆☆

Требуется реализовать методы в `urban_dictionary.py`

Вы создали проект “Словаря Нового Русского” языка, и поддерживаете список новых слов, которые недавно появились в языке.

```python
new_russian_dictionary = ["Контент", "Лутер", "Тренд", "Фиксер", "Фэшн", "Хипстер"]
```

Как и в любом словаре, у вас слова идут строго порядку.
Напишите функцию которая будет вставлять в словарь новые слова,

```python
def insert_new_word(word: str):
    # TODO please implement
```

### 2. Мидер, где ганги?
★★★☆☆

Требуется реализовать методы в `doka4.py`

На самом деле мы немного промахнулись с добавлением нового игрока в нашу очередь.
Если игрока с таким рейтингом в очереди нет, то действительно мы вставим элемент на нужную позицию.
Однако если в очереди уже есть другие игроки с таким же рейтингом, то мы вставим нового игрока в первым среди равных ему, хотя по логике нашей очереди должны вставить последним.
Для того чтобы добиться этого нам нужно реализовать функцию поиска “последнего среди равных”,
т.е. самого правого элемента с таким же рейтингом.

```python
def search_rightmost_player_with_rating(queue: List[Player], rating_band: int) -> int:
    # TODO Релизуйте функцию поиска "последнего среди равных"
    return -1

def insert_player_in_queue_with_shift(queue: List[Player], index: int, new_player: Player) -> None:
    # TODO Реализуйте вставку в очередь (в списке queue гарантированно будет свободное место)
    pass
```
