from typing import List


def permutate_words(words: List[str]) -> None:
    i = 0
    while i < len(words) - 1:
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                words[i] = words[i][1:] + words[i][0]
                i = 0
        i += 1


words = [
    'шбака',
    'катeнк',
    'гусък',
    'шбака',
    'бакаш'
]
permutate_words(words)
print(words)