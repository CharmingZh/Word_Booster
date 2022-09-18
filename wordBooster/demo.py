import linecache


def ana_str(line_str):
    [diff, num, ch, fre, pron, mean] = line_str.strip().split('=')
    return diff, num, ch, fre, pron, mean


if __name__ == '__main__':
    file_path = r'.data_storage/word.txt'
    for i in range(233, 444):
        print(ana_str(linecache.getline(file_path, i)))
