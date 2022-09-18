import pdfplumber
import os
"""
    pdfplumber.PDF.metadata
                  .pages.page_number
                        .width
                        .height
                        .objects/.chars/.lines/.rects/  这些属性中的每一个都是一个
                        .curves/.figures/.images        列表，并且每个列表针对嵌入
                                                        面上的每个此类对象包含一个
                                                        字典。
"""


def pdf_to_txt(pdf_t, page_lst, name):
    file_name = 'wordBooster/data_preprocess/' + name + '.txt'
    file = open(file_name, "w")
    for page_num in page_lst:
        for line in pdf_t.pages[page_num].extract_table():
            temp = []
            for item in line:
                if item == '' or item == 'ⒶⒷⒸ' or item is None:
                    continue
                temp.append(item)
            if len(temp) != 5:
                print(temp)
            for item in temp:
                write_str = str(item) + '\t'
                write_str.replace("\n", '')
                file.write(write_str)
            file.write('\n')
    file.close()


def transmit_process():
    pdf = pdfplumber.open('wordBooster/data_preprocess/vocabulary.pdf')
    A_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    B_lst = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
             32]
    C_lst = [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
             51, 52, 53, 54, 55, 56, 57]
    D_lst = [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76,
             77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,
             94, 95, 96, 97, 98]
    E_lst = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
    F_lst = [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
             127, 128, 129, 130, 131]
    pdf_to_txt(pdf, A_lst, 'A_word_data')
    pdf_to_txt(pdf, B_lst, 'B_word_data')
    pdf_to_txt(pdf, C_lst, 'C_word_data')
    pdf_to_txt(pdf, D_lst, 'D_word_data')
    pdf_to_txt(pdf, E_lst, 'E_word_data')
    pdf_to_txt(pdf, F_lst, 'F_word_data')
    print('Done')


def read_from_txt(section):
    file_path = 'wordBooster/data_preprocess/' + section + '_word.txt'
    file = open(file_path, "r")
    result = open('wordBooster/data_preprocess/word_temp.txt', 'a')
    for line in file:
        if len(line.split('\t')) == 5:
            line = line.split('\t')
            line[4] = line[4].replace('\n', '')
        else:
            line = line.split('\t')[:-1]
        write_str = '='.join(line)
        write_str = section + '=' + write_str + '\n'
        result.write(write_str)
    file.close()
    result.close()
    print('done')


if __name__ == '__main__':
    # transmit_process()
    read_from_txt('A')
    read_from_txt('B')
    read_from_txt('C')
    read_from_txt('D')
    read_from_txt('E')
    read_from_txt('F')

