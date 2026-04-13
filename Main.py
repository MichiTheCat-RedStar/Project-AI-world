# Данный код распространяется по MIT лицензии автором MichiTheCat
# Не видитесь на проекты, выдающие себя за оригинал или подобное
# Оригинал кода https://github.com/MichiTheCat-RedStar/Project-AI-world


# Инициализация (для кода)

try: # Библиотеки
    print('- Импорт библиотек...', end='', flush=True)
    import ollama
    import os
    from time import sleep
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib # pip install tomli если ваш python не имеет tomlib
except Exception as error:
    print(f'\r! Импорт библиотек не завершён! Ошибка: {error}')
else:
    print('\r+ Импорт библиотек завершён.')

try: # Проверка целостности                     v какой файл | действие при повреждении
    print('- Проверка файлов...', end='', flush=True)
    os.makedirs('./logs', exist_ok=True)        # logs | Восстановление при повреждении
    if not os.path.exists('./.gitignore'):      # .gitignore | Восстановление при повреждении
        with open('./.gitignore', 'w') as file:
            file.write('logs/*')
    if not os.path.exists('./LICENSE'):         # LICENSE | Восстановление при повреждении
        with open('./LICENSE', 'w') as file:
            file.write('MIT License\n\nCopyright (c) 2026 Michi The Cat\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.')
    if not os.path.exists('./prompts.toml'):    # prompts.toml | Пустой файл при повреждении
        with open('./prompts.toml', 'w') as file:
            pass
    if not os.path.exists('./README.md'):       # README.md | Пустой файл при повреждении
        with open('./README.md', 'w') as file:
            pass
    if not os.path.exists('./settings.toml'):   # settings.toml | Пустой файл при повреждении
        with open('./settings.toml', 'w') as file:
            pass
except Exception as error:
    print(f'\r! Проверка файлов не завершена! Ошибка: {error}')
else:
    print('\r+ Проверка файлов завершена.')

try: # Загрузка переменных из настроек (settings.toml)
    print('- Инициализация настроек...', end='', flush=True)
    with open('settings.toml', 'rb') as file: # settings.toml/...
        data = tomllib.load(file)
        WorldSize = { # ./codespace/world_{xy} -> WorldSize['{XY}']
            'X': int(data['codespace']['world_x']),
            'Y': int(data['codespace']['world_y']) }
        ModelSettings = { # ./model/... -> ModelSettings[*]
            'model': str(data['model']['model']),   # ./model -> ModelSettings['model']
            'CPU': int(data['model']['CPU']) }      # ./CPU -> ModelSettings['CPU']
        del data
except Exception as error:
    print(f'\r! Инициализация настроек не завершена! Ошибка: {error}')
else:
    print('\r+ Инициализация настроек завершена.')

try: # Загрузка промптов (prompts.toml)
    print('- Инициализация промптов...', end='', flush=True)
    with open('prompts.toml', 'rb') as file: # prompts.toml/...
        data = tomllib.load(file)
        Prompts = {
            'believer': str(data['Believer']).strip(),          # Believer
            'atheistic': str(data['Atheistic']).strip(),        # Atheistic
            'instruction': str(data['Instruction']).strip() }   # Instruction
        del data
except Exception as error:
    print(f'\r! Инициализация промптов не завершена! Ошибка: {error}')
else:
    print('\r+ Инициализация промптов завершена.')


# Инициализация (для мира)

World, step = [], 0
for y in range(WorldSize['Y']):
    World.append([])
    for x in range(WorldSize['X']):
        World[y].append('.')

def Show() -> None:
    'Функция для отображения всего поля `World`'
    for y in World:
        print(''.join([str(x) for x in y]))


# Инициализация (AI NPC)

NPCs = []

class NPC: # TODO: я всё ещё не понимаю полностью принцип классов и этого ООП, а только тыкаю на угад "Правильно ли?"...
    'AI NPC создания мира'
    def __init__(self, prompt:str):
        '`prompt` должно быть задано "believer" или "atheistic"' # TODO доработать в будущем
        self.health = 10        # Здоровье
        self.hunger = 10        # Голод
        self.prompt = prompt    # Промпт
        self.alive = True       # Живой?

    def Touch(self) -> None:
        'Функция, чтобы обновить сущность на один тик'
        if self.alive:
            self.hunger -= 1
            if self.hunger < 1:
                self.health -= 1
            if self.hunger < 0:
                self.hunger = 0
            if self.health < 1:
                self.alive = False


# Основной цикл

print('\nНажмите Ctrl+C для вызова консоли...')

a = NPC('believer')
while True:
    try:
        step += 1
        print(f'\nДля меню нажмите Ctrl+C | Шаг: {step}')
        Show()
        sleep(1)
        # NPC.Touch(a)
        a.Touch()   # TODO тут поле для эксперементов, данный код будет полностью изменён в будущем (речь о работе с классом, а не обработке Ctrl+C)
        # a.hunger -= 1
        print(a.hunger)
    except KeyboardInterrupt: # Ctrl+C меню
        print('\nКонсоль взвана, пропишите "help" для помощи...')
        while True:
            User = input('\n> ').strip().lower()
            if User == '':
                pass
            elif User == 'back':
                break
            elif User == 'exit':
                print('Удачи!')
                quit()
            elif User == 'help':
                print('''
back - выйти из Ctrl+C меню
exit - выйти из программы
help - список всех команд
                      '''.strip())
            else:
                print(f'"{User}" не является встроенной командой!')
    except Exception as error:
        input(f'\nОшибка: {error}\n[Нажмите ENTER чтобы продолжить]')