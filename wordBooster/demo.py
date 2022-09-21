import linecache
import os.path
import random


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
    print("----------------------------------------\n")  # 2 lines
    word_ch = get_word(word_num, 1)
    word_str = ':::::' + ' ' * ((30 - len(word_ch)) // 2) \
               + word_ch \
               + ' ' * ((30 - len(word_ch)) // 2) + ':::::'
    print(word_str)
    while True:
        print("\n----------------------------------------\n")  # 2 lines
        select = input(
            "Do you know this word?   Your response: "
        )
        if select == 'y':
            word_mean = get_word(word_num, 4)
            select_str = "Are you sure? " + word_mean + '  Your response: '
            select = input(select_str)
            if select == 'y':
                print("----------------------------------------\n")
                return True
            elif select == 'n':
                print("----------------------------------------\n")
                return False
        elif select == 'n':
            print('No')
            print("----------------------------------------\n")
            return False


if __name__ == '__main__':
    print("|      为了更好的使用体验，请拉动窗口至恰好包围这两段文字。           |\n")
    print("       Welcome to the ...")
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
    print("       Global learning progress pointer get.")

    print("       Checking data completeness ... ")
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
        # FIXME: Remember to RESET the learning plan!!!!
        for i in range(GLOBAL_PROGRESS_POINTER + 1,
                       GLOBAL_PROGRESS_POINTER + 50 + 1):
            WORDS_CURRENT.append(i)
    # 三级学习队列
    WORDS_LV_1 = []
    WORDS_LV_2 = []
    WORDS_LV_3 = []

    # 本轮学习将要复习的旧词(index)列表
    WORDS_BEFORE = []
    if not linecache.getline(user_work_path, 2):
        print("       No historical data to be loaded, initializing...")
    else:
        print("       Reading historical learning cache.")
        WORDS_BEFORE = list(
            map(
                int,
                linecache.getline(user_work_path, 2).split(' ')
            )
        )

    print(
        "\n| 累积学习", GLOBAL_PROGRESS_POINTER, "词, 剩余",
        word_file_count - GLOBAL_PROGRESS_POINTER, "词    .. 按 Enter 继续 |",
        end='')
    char_temp = input()

    # better_viewer()
    """
    print("  _____                       _   __ ")
    print(" |  __ \                     | | /_ |")
    print(" | |__) |___  _   _ _ __   __| |  | |")
    print(" |  _  // _ \| | | | '_ \ / _` |  | |")
    print(" | | \ \ (_) | |_| | | | | (_| |  | |")
    print(" |_|  \_\___/ \__,_|_| |_|\__,_|  |_|")
    """
    for word_num in WORDS_CURRENT:
        print("  _____                       _   __ ")
        print(" |  __ \                     | | /_ |")
        print(" | |__) |___  _   _ _ __   __| |  | |")
        print(" |  _  // _ \| | | | '_ \ / _` |  | |")
        print(" | | \ \ (_) | |_| | | | | (_| |  | |")
        print(" |_|  \_\___/ \__,_|_| |_|\__,_|  |_|\n")
        if judge_word(word_num) is True:
            continue
        else:
            WORDS_LV_1.append(word_num)

    # LEVEL 1 QUEUE
    print("***        First round done. ",
          (len(WORDS_LV_1) * 10) / 5,
          "% unrecognized, fighting!       ***")
    count_temp = 0
    for word_num in WORDS_LV_1:
        if count_temp == 10:
            count_temp = 0
            char_temp = input("Press Enter to continue: ")
        print(
            word_num, '\t',
            get_word(word_num, 1), '\t',
            get_word(word_num, 4), '\t',
            get_word(word_num, 3)
        )
        count_temp += 1
    char_temp = input("Press Enter to continue: ")
    random.shuffle(WORDS_LV_1)

    # LEVEL 2 QUEUE
    for word_num in WORDS_LV_1:
        print("  _                    _   __ ")
        print(" | |                  | | /_ |")
        print(" | |     _____   _____| |  | |")
        print(" | |    / _ \ \ / / _ \ |  | |")
        print(" | |___|  __/\ V /  __/ |  | |")
        print(" |______\___| \_/ \___|_|  |_|\n")
        if judge_word(word_num) is True:
            continue
        else:
            WORDS_LV_2.append(word_num)

    print("***        Second round done. ",
          (len(WORDS_LV_2) * 10) / 5,
          "% unrecognized, fighting!       *** ")
    count_temp = 0
    for word_num in WORDS_LV_2:
        if count_temp == 10:
            count_temp = 0
            char_temp = input("Press Enter to continue: ")
        print(
            word_num, '\t',
            get_word(word_num, 1), '\t',
            get_word(word_num, 4), '\t',
            get_word(word_num, 3)
        )
        count_temp += 1
    char_temp = input("Press Enter to continue: ")
    random.shuffle(WORDS_LV_2)

    # LEVEL 3 QUEUE
    for word_num in WORDS_LV_2:
        print("  _                    _   ___  ")
        print(" | |                  | | |__ \ ")
        print(" | |     _____   _____| |    ) |")
        print(" | |    / _ \ \ / / _ \ |   / / ")
        print(" | |___|  __/\ V /  __/ |  / /_ ")
        print(" |______\___| \_/ \___|_| |____|\n")
        if judge_word(word_num) is True:
            continue
        else:
            WORDS_LV_3.append(word_num)
    print("***       Second round done. ",
          (len(WORDS_LV_3) * 10) / 5,
          "% unrecognized, fighting!       ***")
    count_temp = 0
    for word_num in WORDS_LV_3:
        if count_temp == 10:
            count_temp = 0
            char_temp = input("Press Enter to continue: ")
        print(
            word_num, '\t',
            get_word(word_num, 1), '\t',
            get_word(word_num, 4), '\t',
            get_word(word_num, 3)
        )
        count_temp += 1
    char_temp = input("Press Enter to continue: ")

    # LEVEL 3 QUEUE
    for word_num in WORDS_LV_3:
        print("  _               _     _____                       _ ")
        print(" | |             | |   |  __ \                     | |")
        print(" | |     __ _ ___| |_  | |__) |___  _   _ _ __   __| |")
        print(" | |    / _` / __| __| |  _  // _ \| | | | '_ \ / _` |")
        print(" | |___| (_| \__ \ |_  | | \ \ (_) | |_| | | | | (_| |")
        print(" |______\__,_|___/\__| |_|  \_\___/ \__,_|_| |_|\__,_|\n")
        judge_word(word_num)
    print("***       Last round done. ")

    temp_list = []

    for word_num in WORDS_BEFORE:
        print("  _____            _                         __  ")
        print(" |  __ \          (_)                ______  \ \ ")
        print(" | |__) |_____   ___  _____      __ |______|  | |")
        print(" |  _  // _ \ \ / / |/ _ \ \ /\ / /  ______   | |")
        print(" | | \ \  __/\ V /| |  __/\ V  V /  |______|  | |")
        print(" |_|  \_\___| \_/ |_|\___| \_/\_/            /_/ \n")
        if judge_word(word_num) is True:
            ALL_WORDS_HISTORY[word_num - 1] += 1
            if ALL_WORDS_HISTORY[word_num - 1] <= 4:
                temp_list.append(word_num)
        else:
            ALL_WORDS_HISTORY[word_num - 1] -= 1
            temp_list.append(word_num)

    for item in WORDS_LV_2:
        temp_list.append(item)
    temp_list.sort()

    # 写入当前进展指针
    temp_file = open(user_info_path, 'w')
    temp_file.write(str(GLOBAL_PROGRESS_POINTER + 50))
    temp_file.close()

    temp_file = open(user_work_path, 'w')
    ALL_WORDS_HISTORY = list(
        map(str, ALL_WORDS_HISTORY)
    )
    write_str = ' '.join(ALL_WORDS_HISTORY)
    temp_file.write(write_str)

    temp_list = list(
        map(str, temp_list)
    )
    write_str = ' '.join(temp_list)
    temp_file.write('\n')
    temp_file.write(write_str)
    temp_file.close()

