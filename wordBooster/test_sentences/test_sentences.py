import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


class DictRstParser:
    def get_content(self, from_obj, selector_str):
        rst = from_obj.select(selector_str)
        if len(rst) == 0:
            return None
        elif len(rst) == 1:
            return rst[0].get_text().replace("\xa0", " ").strip()
        else:
            return '\n'.join([e.get_text() for e in rst])

    def __init__(self, word_str):
        self.req_link = f"https://cn.bing.com/dict/search?q={word_str}"
        self.res_txt = requests.get(self.req_link).text
        self.soup = BeautifulSoup(self.res_txt, 'html.parser')
        self.word_info_selector_dict = {
            'word': 'div#headword',
            'eng_pr': 'div.hd_pr',
            'ame_pr': 'div.hd_prUS',
            'tongyi': 'div.wd_div',
            'fushu': 'div.hd_div1',
            'defination': 'div.qdef > ul > li',
        }
        self.word_info_dict = {}
        self.related_divs = self.soup.select('div.lf_area > div')
        for k, v in self.word_info_selector_dict.items():
            self.word_info_dict[k] = self.get_content(self.related_divs[0], v)

        self.word_info_dict['sentences'] = self.get_content(
            self.related_divs[1], 'div#sentenceSeg')


if __name__ == '__main__':
    with open('data.txt', 'r') as wordlistfile:
        word_list = wordlistfile.readlines()

    row_list = []

    for w in word_list:
        parser = DictRstParser(w)
        row_list.append(parser.word_info_dict)
        time.sleep(0.5)

    df = pd.DataFrame(row_list)

    xlwriter = pd.ExcelWriter('wordlist.xlsx', engine='xlsxwriter')
    df.to_excel(xlwriter, 'Sheet0')
    xlwriter.save()
