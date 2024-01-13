def happy_new_year(seg: int):
    print(' ' * seg + '<>')
    for lvl in range(1, seg + 1):
        for i in range(0, lvl):
            print(' ' * (seg - i) + '/' + ' ' * 2 * i + chr(92))
        print(' ' * (seg - i - 1) + '/' + '_' * 2 * (i + 1) + chr(92))
    print(' ' * seg + '||')
def favourite_number() -> int:
    return 1
def sequence_element(n: int):
    return int((1 + (1 + 8*(n-1))**0.5)/2)



#Задания с файлами у меня так сделаны:
def unix2dos(filename: str):
    f = open(filename, "r")
    s = f.read()
    new = s.replace(chr(10), chr(10) + chr(13))
    with open (filename, "w") as f:
        f.write('')
        f.write(new)
    f.close()


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
