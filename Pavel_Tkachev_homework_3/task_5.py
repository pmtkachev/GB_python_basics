from random import choice


def get_jokes(n, repeat=True):
    """Функция возвращает определенное количество сгенерированных шуток,
    где n - количество. Флаг repeat отвечает за повтор слов в шутках. При repeat=False,
    если количество указано больше, чем слов списках, обрабатываем исключение."""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if repeat:
        jokes = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for i in range(n)]
    else:
        jokes = []
        try:
            for i in range(n):
                noun = choice(nouns)
                adverb = choice(adverbs)
                adjective = choice(adjectives)
                jokes.append(f'{noun} {adverb} {adjective}')
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
        except IndexError:
            return 'Указанное количество слов больше, чем есть в списках'
    return jokes


print(get_jokes(5))
print(get_jokes(8))
print(get_jokes(4, repeat=False))
print(get_jokes(6, repeat=False))
