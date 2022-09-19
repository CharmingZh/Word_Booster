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


def better_viewer():
    print()
    print("|      为了更好的使用体验，请拉动窗口至恰好包围这两段文字。      |")
    for _ in range(0, 20):
        print()
    print("|      为了更好的使用体验，请拉动窗口至恰好包围这两段文字。      |")


def user_status():
    file_path = r'.data_storage/.self.txt'
    if os.path.exists(file_path) is False:
        user_file = open(file_path, 'w')
        user_file.write('0\n')
        user_file.write('0')


def judge_word(num):
    print("----------------------------------------")
    print()
    word_ch = get_word(word_num, 1)
    word_str = ':::::' + ' ' * ((30 - len(word_ch)) // 2) \
               + word_ch \
               + ' ' * ((30 - len(word_ch)) // 2) + ':::::'
    print(word_str)


if __name__ == '__main__':
    print("Welcome to the ...")
    print(" *     _    _               _______                 _           ")
    print(" *    | |  | |             | | ___ \               | |          ")
    print(" *    | |  | | ___  _ __ __| | |_/ / ___   ___  ___| |_ ___ _ __ ")
    print(" *    | |/\| |/ _ \| '__/ _` | ___ \/ _ \ / _ \/ __| __/ _ \ '__|")
    print(" *    \  /\  / (_) | | | (_| | |_/ / (_) | (_) \__ \ ||  __/ |   ")
    print(" *     \/  \/ \___/|_|  \__,_\____/ \___/ \___/|___/\__\___|_|   ")
    print("            ...   designed by : Jmzhang@bjfu.edu.cn  ...  ")
    print("                                   ... word Booster Starting ... ")

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

    """
    user_info_file = open(user_info_path, 'r+')
    user_work_file = open(user_work_path, 'r+')
    """

    # 用户的当前学习进度指针
    GLOBAL_PROGRESS_POINTER = int(linecache.getline(user_info_path, 1))
    print("Global learning progress pointer get.")

    print("Checking data completeness ... ")
    # 所有单词的历史学习数据
    ALL_WORDS_HISTORY = list(
        map(
            int,
            linecache.getline(user_work_path, 1).split(' ')
        )
    )
    print("                   ... learning details, done")

    # 本轮要学习的词汇(index)列表
    WORDS_CURRENT = []
    if word_file_count - GLOBAL_PROGRESS_POINTER < 50:
        for i in range(GLOBAL_PROGRESS_POINTER, word_file_count + 1):
            WORDS_CURRENT.append(i)
    else:
        for i in range(GLOBAL_PROGRESS_POINTER + 1, 50 + 1):
            WORDS_CURRENT.append(i)

    # 三级学习队列
    WORDS_LV_1 = []
    WORDS_LV_2 = []
    WORDS_LV_3 = []

    # 本轮学习将要复习的旧词(index)列表
    WORDS_BEFORE = []
    if not linecache.getline(user_work_path, 2):
        print("No historical data to be loaded, initializing...")
    else:
        print("Reading historical learning cache.")
        WORDS_BEFORE = list(
            map(
                int,
                linecache.getline(user_work_path, 2).split(' ')
            )
        )
    better_viewer()
    for word_num in WORDS_CURRENT:
        temp = input()
        judge_word(word_num)


