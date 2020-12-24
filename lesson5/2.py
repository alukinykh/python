# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task_2.txt') as f_obj:
    content = f_obj.readlines()
    for key, line in enumerate(content):
        count_words = len(line.split())
        print(f'{key + 1} строка - {count_words} слов(а)')
    print(f'Всего {len(content)} строк')
