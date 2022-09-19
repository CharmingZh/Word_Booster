import linecache
import os.path


def ana_str(line_str):
    [diff, num, ch, fre, pron, mean] = line_str.strip().split('=')
    return diff, num, ch, fre, pron, mean


def get_word(num, select):
    file_path = r'.data_storage/word.txt'
    diff, num, ch, fre, pron, mean = ana_str(linecache.getline(file_path, num))
    retVal = 0
    match select:
        case 0:
            retVal = diff
        case 1:
            retVal = ch
        case 2:
            retVal = fre
        case 3:
            retVal = pron
        case 4:
            retVal = mean
    return retVal


def user_status():
    file_path = r'.data_storage/.self.txt'
    if os.path.exists(file_path) is False:
        user_file = open(file_path, 'w')
        user_file.write('0\n')
        user_file.write('0')


if __name__ == '__main__':

    word_file_count = 5201

    user_info_path = r'.data_storage/.self.txt'
    user_work_path = r'.data_storage/.work.txt'

    if os.path.exists(user_info_path) is False:
        print("Initialization Processing...")
        temp_file = open(user_info_path, 'w')
        temp_file.write('0')

        temp_file.close()
    if os.path.exists(user_work_path) is False:
        print("         ...still...         ")
        temp_file = open(user_work_path, 'w')
        write_list = ['0'] * word_file_count
        write_str = ' '.join(write_list)
        temp_file.write(write_str)
        temp_file.close()
        print("                         ...Done")

    user_info_file = open(user_info_path, 'r+')
    user_work_file = open(user_work_path, 'r+')



