try:    # Импорт библиотек
    print('… Импорт библиотек...', end='')
    import os
    import ollama
except Exception as e: print('\b'*32+'› Импорт библиотек не удался !!! Причина: ', e)
else: print('\b'*32+'• Импорт библиотек завершён')


try:    # Настройка видимости символов
    print('… Настройка видимости символов..', end='')
    os.system('chcp 65001 > nul')
except Exception as e: print('\b'*32+'› Настройка видимости символов не удалась !!! Причина: ', e)
else: print('\b'*32+'• Настройка видимости символов завершена')


try:    # Создание папок при отсутствии
    print('… Проверка папок...', end='')
    os.makedirs('./Logs', exist_ok=True)        # Logs
    os.makedirs('./World', exist_ok=True)       # World
except Exception as e: print('\b'*32+'› Проверка папок не удалась !!! Причина: ', e)
else: print('\b'*32+'• Проверка папок завершена')


try:    # Проверка целостности файлов
    print('… Проверка целостности файлов...', end='')
    if os.path.exists('Prompt'): pass           # Promp
    else:
        with open('Prompt', 'w') as f: pass
    if os.path.exists('ReadMe.txt'): pass       # ReadMe.txt
    else:
        with open('ReadMe.txt', 'w') as f: pass
    if os.path.exists('Requirements.bat'): pass # Requirements.bat
    else:
        with open('Requirements.bat', 'w') as f: pass
    if os.path.exists('Save'): pass             # Save
    else:
        with open('Save', 'w') as f: pass
    if os.path.exists('Settings.txt'): pass     # Settings.txt
    else:
        with open('Settings.txt', 'w') as f: pass
except Exception as e: print('\b'*32+'› Проверка целостности файлов не удалась !!! Причина: ', e)
else: print('\b'*32+'• Проверка целостности файлов завершена')


try:    # Загрузка настроек
    print('… Загрузка настроек...', end='')
    with open('Settings.txt', 'r') as f:
        f = f.read()
        f = f.split('\n')
        for line in f:
            if line[:5] == 'Model': MODEL = line[6:]
            elif line[:3] == 'CPU': CPU = int(line[4:])
except Exception as e: print('\b'*32+'› Загрузка настроек не удалась !!! Причина: ', e)
else: print('\b'*32+'• Загрузка настроек завершена')