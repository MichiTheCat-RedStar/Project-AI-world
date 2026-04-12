# Данный код распространяется по MIT лицензии автором MichiTheCat
# Не видитесь на проекты, выдающие себя за оригинал или подобное
# Оригинал кода https://github.com/MichiTheCat-RedStar/Project-AI-world


# Инициализация

try: # Библиотеки
    print('- Импорт библиотек...', end='', flush=True)
    import ollama
    import os
except Exception as error:
    print(f'\r! Импорт библиотек не завершён! Ошибка: {error}')
else:
    print('\r+ Имопрт библиотек завершён.')

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

try: # Загрузка переменных из настроек (settings.toml)      TODO: Сделать загрузку settings.toml
    print('- Инициализация настроек...', end='', flush=True)
except Exception as error:
    print(f'\r! Инициализация настроек не завершена! Ошибка: {error}')
else:
    print('\r+ Инициализация настроек завершена.')

try: # Загрузка промптов (prompts.toml)                     TODO: Сделать загрузку prompts.toml
    print('- Инициализация промптов...', end='', flush=True)
    Prompts = {     # TODO: Сделать из prompts.toml звгрузку переменных в словарь
        'believer': None,
        'atheistic': None
    }
except Exception as error:
    print(f'\r! Инициализация промптов не завершена! Ошибка: {error}')
else:
    print('\r+ Инициализация промптов завершена.')


# Основной цикл

print('\nНажмите Ctrl+C для выхода...')
while True:
    pass    # TODO: Доделать