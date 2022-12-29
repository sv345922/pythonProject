"""
>>> search_rightmost_player_with_rating(ratings, 4000)
7
>>> search_rightmost_player_with_rating(ratings, 5000)
7
>>> search_rightmost_player_with_rating(ratings, 3500)
6
>>> search_rightmost_player_with_rating(ratings, 3000)
6
>>> search_rightmost_player_with_rating(ratings, 1600)
5
>>> search_rightmost_player_with_rating(ratings, 1000)
0
>>>
"""
from typing import List


class Player:
    def __init__(self, rating: int, nick_name: str) -> None:
        self.rating = rating
        self.nick_name = nick_name


def search_rightmost_player_with_rating(queue: List[Player], ratingBand: int) -> int:
    """возвращает индекс места вставки для новой позиции с рейтингом ratingBand, смещенный вправо"""
    left = 0
    right = len(queue)
    while left < right:
        middle = (left + right) // 2
        if queue[middle].rating > ratingBand:
            right = middle
        else:
            left = middle + 1
    return right

def insert_player_in_queue_with_shift(queue: List[Player], index: int, new_player: Player) -> None:
    """вставляет в список queue новый элемент new_player в позицию index
    >>> insert_player_in_queue_with_shift(ratings, search_rightmost_player_with_rating(ratings, new_player.rating), new_player)
    >>> for item in ratings:
    ...        print(item.rating, item.nick_name)
    1100 Crowbar Freeman
    1200 London Mollarik
    1600 Raziel of Kain
    1600 Gwinter of Rivia
    1600 Slayer of Fate
    1600 Shmike
    3000 Jon Know
    4000 Caius Cosades

    """
    queue.append("")
    for i in range(len(queue) - 1, index, -1):
        queue[i] = queue[i - 1]
    queue[index] = new_player

new_player = Player(1600, "Shmike")
ratings = [Player(1100, "Crowbar Freeman"),   # 0
            Player(1200, "London Mollarik"),   # 1
            Player(1600, "Raziel of Kain"),    # 2
            Player(1600, "Gwinter of Rivia"),  # 3
            Player(1600, "Slayer of Fate"),    # 4
            # Player(1600, "Shmike"),
            Player(3000, "Jon Know"),          # 5
            Player(4000, "Caius Cosades"),     # 6
        ]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


