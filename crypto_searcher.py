import os
import sys
import random
import time
import pickle

import stdiomask
from colorama import init, Fore, Back, Style
from progress.bar import ChargingBar, Bar
from termcolor import cprint 
from pyfiglet import figlet_format

from wordlist import WORDLIST
from logins import logins
from bars import bars

balance = 0
tokens = 0
nft = 0

with_balance = 0 
all_checks = 0 
founded = 0


def on_startup():
    global title 
    global all_checks
    init(strip=not sys.stdout.isatty())
    first = False
    if not os.path.exists('log.txt'):
        log = open('log.txt', 'w+')
        log.close()
        first = True
    if not os.path.exists('tokens.txt'):
        log = open('tokens.txt', 'w+')
        first = True
        log.close()
    if not os.path.exists('data'):
        log = open('data', 'w+')
        first = True
        log.close()
    if first:
        installing()
    try: 
        with open('data', 'rb') as f:
            all_checks = pickle.load(f)
    except: 
        all_checks = 0
    title = f'С балансом: {with_balance} - Всего проверок: {all_checks} - [Нашли {founded}$]'
    os.system("title " + title)
    cprint(figlet_format('New Gold Farm', font='starwars'),
       'white', 'on_blue', attrs=['bold'])
    print('\n')
    login = stdiomask.getpass(prompt=Fore.BLUE + 'Введите логин: ', mask='*')
    password = stdiomask.getpass(prompt=Fore.BLUE + 'Введите пароль: ', mask='*')
    if login in list(x[0] for x in logins) and password in list(x[1] for x in logins):
        result = True
    else:
        result = False
    animation('Обработка данных ', 5)
    if result:
        print('Начинаем работу...')
        time.sleep(3)
        os.system('cls||clear')
        return True
    elif not result:
        print(Fore.RED + 'Данные для авторизации неверны, либо программа уже используется на другом устройстве.\n' +
                'За лицензией обратитесь к t.me/ngf_admin')
        time.sleep(3)
        return False

def working():
    while True:
        text = f'Balance: 0 | Tokens: 0 | NFT: 0 | Mnemonic phrase: {generate_phrase(WORDLIST)}\n'
        print(Fore.BLUE + Style.BRIGHT + text)

def generate_phrase(list_: list) -> str:
    global all_checks
    global title
    phrase = ''
    for i in range(12):
        word = random.choice(list_)
        if word not in phrase:
            phrase += word + ' '
        latency = random.choice([0.03, 0.04, 0.05, 0.035, 0.045,
            0.01, 0.04, 0.01, 0.035, 0.045,
            0.01, 0.04, 0.01, 0.035, 0.045,
            0.01, 0.04, 0.01, 0.035, 0.045,
            0.01, 0.04, 0.01, 0.035, 0.045,
            0.01, 0.04, 0.01, 0.035, 0.045,
            0.01, 0.04, 0.01, 0.035, 0.045,
            0.2])
        time.sleep(latency)
    all_checks += 1
    title = f'С балансом: {with_balance} - Всего проверок: {all_checks} - [Нашли {founded}$]'
    if sys.platform == 'win32':
        os.system("title " + title)
    with open('data', 'wb') as f:
        pickle.dump(all_checks, f)
    return phrase

def main():
    on_startup()
    login = working()
    if login:
        working()
    else:
        sys.exit()

# Soft installing animation
def installing():
    animation('Подготовка к установке утилит ', 3)
    for bar in bars:
        with bar:
            for i in range(bar.max):
                sleep = random.choice([0.02, 0.01, 0.01, 0.01, 0.02, 0.03, 0.1, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
                time.sleep(sleep)
                bar.next()
    animation('Распаковка ', 3)
    os.system('cls||clear')

# Loading animation
def animation(text: str = '', time_: int = 3):
    animation = "|/-\\"
    idx = 0
    while idx < (time_ * 10):
        print(text + animation[idx % len(animation)] + "\r", end='')
        idx += 1
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        try:
            print(animation(Fore.WHITE + 'Сохранение прогресса', 1))
        except KeyboardInterrupt:
            sys.exit()
            