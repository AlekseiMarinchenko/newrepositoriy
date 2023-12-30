def happy_new_year(seg: int):
    print(' ' * seg + '<>')
    for lvl in range(1, seg + 1):
        for i in range(0, lvl):
            print(' ' * (seg - i) + '/' + ' ' * 2 * i + chr(92))
        print(' ' * (seg - i - 1) + '/' + '_' * 2 * (i + 1) + chr(92))
    print(' ' * seg + '||')
happy_new_year(10)


def consequence(n: int):
    def func():
        return lambda x: (x - 2)*(x-13)*(x-2023)*(x - 2024)/((1-2)*(1 - 13)*(1 -2023)*(1-2024)) +2* (x - 1)*(x-13)*(x-2023)*(x - 2024)/((2-1)*(2 - 13)*(2 -2023)*(2-2024)) + 6*(x - 2)*(x-1)*(x-2023)*(x - 2024)/((13-2)*(13 - 1)*(13 -2023)*(13-2024)) + 64*(x - 2)*(x-13)*(x-1)*(x - 2024)/((2023-2)*(2023 - 13)*(2023 - 1)*(2023 - 2024)) + 64*(x - 2)*(x-13)*(x-2023)*(x - 1)/((2024-2)*(2024 - 13)*(2024 -2023)*(2024 - 1))
    return func()(n)
print(consequence(2024))


def unix2dos(filename: str):
    f = open(filename, "r")
    s = f.read()
    new = s.replace(chr(10), chr(10) + chr(13))
    with open (filename, "w") as f:
        f.write('')
        f.write(new)
    f.close()
#Функция unix2dos не факт что работает, так как мы хз как ее проверить на правильность. Питон работает в аски, а юникс и дос он тупо переводит в аски, так что проверьте если знаете как. 

def json2yaml_noexcept(filename):
    import json
    import yaml
    from pathlib import Path
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        yaml_filename = Path(filename).with_suffix('.yaml')
        with open(yaml_filename, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        return data
    except Exception as ex:
        return {'exception': ex}
result = json2yaml_noexcept('New document 1.json')
print(result)

#Задание с 4 програмистами мы поняли как делать только споткнулись на последнем этапе. Нужно посчитать интеграл на промежутке от 0 до 107 включительно, для функции x^(ix), где i - мнимая единица. Кто сможет как-нить это посчитать напишите нам пжл
