from itertools import permutations


def func(alphabet, min_len, max_len):
    joiner = ''.join
    for idx in range(min_len, max_len + 1):
        yield from map(joiner, permutations(alphabet, idx))


d = {
    'Четыре': 4,
    'Пять': 5,
    'Шесть': 6,
    'Семь': 7,
    'Восемь': 8,
    'Девять': 9,
    'Десять': 10,
}

txt = 'gfg'
res = func(txt, 0, 3)

res = set(res)
length = ''

for k, v in d.items():
    if v == len(set(res)):
        length += k

print(f'Строка: {txt}\n'
      f'Результат: {len(set(res))}\n'
      f'{length} различных подстрок: {set(res)}')
