try:    # Импорт библиотек
    print('… Импорт библиотек...', end='', flush=True)
    import os
    import ollama
    import json
    from datetime import datetime
except Exception as e: print('\b'*32+'› Импорт библиотек не удался !!! Причина:', e)
else: print('\b'*32+'• Импорт библиотек завершён')


try:    # Создание папок при отсутствии
    print('… Проверка папок...', end='', flush=True)
    os.makedirs('./Logs', exist_ok=True)                # Logs
    os.makedirs('./World', exist_ok=True)               # World
except Exception as e: print('\b'*32+'› Проверка папок не удалась !!! Причина:', e)
else: print('\b'*32+'• Проверка папок завершена')


try:    # Проверка целостности файлов
    print('… Проверка целостности файлов...', end='', flush=True)
    if os.path.exists('Prompt'): pass                   # Promp
    else:
        with open('Prompt', 'w') as f: pass
    if os.path.exists('ReadMe.txt'): pass               # ReadMe.txt
    else:
        with open('ReadMe.txt', 'w') as f: pass
    if os.path.exists('Requirements.bat'): pass         # Requirements.bat
    else:
        with open('Requirements.bat', 'w') as f: pass
    if os.path.exists('Save'): pass                     # Save
    else:
        with open('Save', 'w') as f: pass
    if os.path.exists('Settings.txt'): pass             # Settings.txt
    else:
        with open('Settings.txt', 'w') as f: pass
except Exception as e: print('\b'*32+'› Проверка целостности файлов не удалась !!! Причина:', e)
else: print('\b'*32+'• Проверка целостности файлов завершена')


try:    # Загрузка настроек
    print('… Загрузка настроек...', end='', flush=True)
    with open('Settings.txt', 'r', encoding='UTF-8') as f:
        f = f.read()
        f = f.split('\n')
        for line in f:
            line = line.split('=')
            if line[0] == 'Model': MODEL = line[1]      # MODEL
            elif line[0] == 'CPU': CPU = int(line[1])   # CPU
except Exception as e: print('\b'*32+'› Загрузка настроек не удалась !!! Причина:', e)
else: print('\b'*32+'• Загрузка настроек завершена')

print(f'{MODEL=}, {CPU=}')