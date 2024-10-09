from sympy import Matrix, pprint
def f(x):
    print('Ступенчатая матрица')
    pprint(x)


print('Введите кол-во строк')
m = int(input())
print('Введите кол-во столбцов')
n = int(input()) + 1
print('Введите построчно матрицу и присоединенный столбец')
matrix = []
for i in range(m):
    matrix.append(input())
for i in range(len(matrix)):
    matrix[i] = matrix[i].split()
for i in range(m):
    for j in range(n):
        matrix[i][j] = int(matrix[i][j])
print(matrix)
augmented_matrix = Matrix(matrix)
row_reduced_matrix, _ = augmented_matrix.rref()
f(row_reduced_matrix)



# def happy_new_year(seg: int):
#     print(' ' * seg + '<>')
#     for lvl in range(1, seg + 1):
#         for i in range(0, lvl):
#             print(' ' * (seg - i) + '/' + ' ' * 2 * i + chr(92))
#         print(' ' * (seg - i - 1) + '/' + '_' * 2 * (i + 1) + chr(92))
#     print(' ' * seg + '||')
# def favourite_number() -> int:
#     return 1
# def sequence_element(n: int):
#     return int((1 + (1 + 8*(n-1))**0.5)/2)



# #Задания с файлами у меня так сделаны:
# def unix2dos(filename: str):
#     f = open(filename, "r")
#     s = f.read()
#     new = s.replace(chr(10), chr(10) + chr(13))
#     with open (filename, "w") as f:
#         f.write('')
#         f.write(new)
#     f.close()


# def json2yaml_noexcept(filename):
#     import json
#     import yaml
#     from pathlib import Path
#     try:
#         with open(filename, 'r') as file:
#             data = json.load(file)
#         yaml_filename = Path(filename).with_suffix('.yaml')
#         with open(yaml_filename, 'w') as file:
#             yaml.dump(data, file, default_flow_style=False)
#         return data
#     except Exception as ex:
#         return {'exception': ex}


# # И вдруг кому-то мое 6-ое понадобиться (Орешников поставил 7, Дашка поставит где-то 4, Федя хз скок)
# #Cсылка на дата сет
# # https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data
# import pandas
# import pandas as pds
# import matplotlib.pyplot as plt
# df = pandas.read_csv('heart_disease_uci.csv')
# plt.figure(figsize=(20,20))
# colors = {'typical angina': 'green', 'asymptomatic': 'blue', 'non-anginal': 'red', 'atypical angina': 'black'}
# plt.scatter(df['age'], df['chol'], c=df['cp'].map(colors), alpha=0.9, s = 10)
# plt.title('Зависимость уровня холестирина от возраста')
# plt.xlabel('Возраст')
# plt.ylabel('Уровень холестерина')
# plt.show()
