from cowsay import cowsay, get_random_cow
import random
import urllib.request
import argparse


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

def custom_cow(text: str) -> None:
    cow = r"""
     \   ^__^             ___wiiiii
      \  (oo)\_______     |
         (__)\ HELLO )\/\/
             ||----w |
             ||     ||
    """
    print(text)
    print(cow)

def ask(prompt: str, valid: list[str] = None) -> str:
    '''
    Функция спрашивает у пользователя слово
    Если необязательный параметр valid не пуст, допустим только ввод слова из valid
    Иначе спрашивает повторно

    :param prompt: str - приглашение к вводу
    :param valid: list[str] - список допустимых слов
    :return: str - введенное пользователем слово
    '''

    while True:
        guess = input(prompt)
        if valid is None or guess in valid:
            return guess
        print(custom_cow("Неверное слово. Попробуйте снова"))


def inform(format_string: str, bulls: int, cows: int) -> None:
    '''
    Функция выводит результат игры

    :param format_string: str - формат вывода
    :param bulls: int - количество быков
    :param cows: int - количество коров
    :return: None
    '''

    print(cowsay(format_string.format(bulls, cows), get_random_cow()))


def main():
    parser = argparse.ArgumentParser(description='Bulls and cows game')
    parser.add_argument('dictionary', help='The dictionary of words')
    parser.add_argument('length', type=int, default=5, nargs='?', help='The length of the words')
    args = parser.parse_args()

    if args.dictionary.startswith('http'):
        with urllib.request.urlopen(args.dictionary) as f:
            words = [word.decode('utf-8').strip() for word in f]
    else:
        with open(args.dictionary) as f:
            words = [word.strip() for word in f]

    words = list(filter(lambda word: len(word) == args.length, words))

    attempts = gameplay(ask, inform, words)
    print(f'Количество попыток: {attempts}')


if __name__ == '__main__':
    main()
