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

print(bullscows("ропот", "полип"))  # -> (1, 1)