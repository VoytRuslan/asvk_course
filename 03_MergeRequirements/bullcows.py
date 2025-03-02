import random


def bullscows(guess: str, secret: str) -> tuple[int, int]:
    '''
    Функция сравнивает догадку игрока с загаданным словом и возвращает количество быков и коров
    В данной игре быки -- это одинаковые буквы, которые в догадке и загадке стоят в одинаковых местах
    Коровы -- это буквы, которые попарно есть и там, и там, но стоят на разных местах

    :param guess: str - догадка, сделанная игроком
    :param secret: str - загаданное слово
    :return: tupe[int, int] - количество быков и коров
    '''
    bulls = 0
    cows = 0
    guess_cows = []
    secret_cows = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        else:
            guess_cows.append(guess[i])
            secret_cows.append(secret[i])
    for cow in set(guess_cows):
        cows += min(guess_cows.count(cow), secret_cows.count(cow))

    return bulls, cows


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    '''
    Функция обеспечивает геймплей игры "Быки и коровы"
    Задумывает случайное слово из списка слов words
    Спрашивает у пользователя слово с помощью функции ask("Введите слово: ", words)
    Выводит пользователю результат с помощью функции inform("Быки: {}, Коровы: {}", b, c)
    Если слово не отгадано, снова спрашивает слово у пользователя

    :param ask: callable - функция, спрашивает у пользователя слово
    :param inform: callable - функция, выводит результат игры
    :param words: list[str] - список слов для загадывания
    :return: int - количество попыток
    '''

    secret = random.choice(words)
    attempts = 0
    while True:
        guess = ask("Введите слово: ", words)
        attempts += 1
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        if bulls == len(secret):
            break
    return attempts
