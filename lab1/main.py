def encode(all_alph, encoded_alf, word):
    res = ""
    for c in word:
        if c in all_alph:
            res += encoded_alf[all_alph.index(c)]
        else:
            res += c
    return res


def decode(all_alph, encoded_alf, word):
    res = ""
    for c in word:
        if c in all_alph:
            res += all_alph[encoded_alf.index(c)]
        else:
            res += c
    return res


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def createDicts(keyword, offset):
    keyword = unique((keyword.upper()))
    full_alph = list()
    for i in range(ord('A'), ord('A') + 26):
        full_alph.append(chr(i))
    for i in range(ord('a'), ord('a') + 26):
        full_alph.append(chr(i))
    for i in range(ord('А'), ord('А') + 32):
        full_alph.append(chr(i))
    full_alph.append('Ё')
    for i in range(ord('а'), ord('а') + 33):
        full_alph.append(chr(i))

    dic = full_alph.copy()
    for c in keyword:
        if c in dic:
            dic.remove(c)
    encoded_alf = ['_'] * len(full_alph)
    for i in range(0, len(keyword)):
        currentOffset = (i + offset) % len(full_alph)
        encoded_alf[currentOffset] = keyword[i]
    for i in range(0, len(dic)):
        currentOffset = (i + offset + len(keyword)) % len(full_alph)
        encoded_alf[currentOffset] = dic[i]
    return full_alph, encoded_alf


def read_file():
    while True:
        path = input("Введите путь к файлу: ").strip()
        try:
            with open(path, encoding='utf-8') as f:
                data = f.readlines()
                return data[0]
        except FileNotFoundError:
            print("Файл не найден!", '\n')
        except ValueError:
            print("Неправильный формат файла!", '\n')


if __name__ == '__main__':
    keyword = input("Введите ключевое слово")
    offset = int(input("Введите отступ (K)"))
    all_alph, encoded_alf = createDicts(keyword, offset)
    print(encode(all_alph, encoded_alf, read_file()))
    print(decode(all_alph, encoded_alf, read_file()))
