from typing import List


class Player:
    def __init__(self, rating: int, nick_name: str) -> None:
        self.rating = rating
        self.nick_name = nick_name


def search_rightmost_player_with_rating(queue: List[Player], ratingBand: int) -> int:
    left = 0
    right = len(queue) - 1
    while left < right:
        middle = (left + right) // 2
        if queue[middle].rating > ratingBand:
            right = middle - 1
        else:
            left = middle
    return right

def insert_player_in_queue_with_shift(queue: List[Player], index: int, new_player: Player) -> None:
    # TODO please implement
    pass
