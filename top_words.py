# (Optional) Week 2 Assignment: Python Word Count
import re
import collections

strip_return = re.compile(r'\n')
words = []
stop_words = []
word_stats = {}

def selecting_words(elim_words, the_words):
    fil_words = [fil_w for fil_w in the_words if fil_w not in elim_words]
    return fil_words

with open('stopwords', mode='r', encoding='utf-8') as s:
    # with open('data/stopwords', mode='r') as s:
    while True:
        sw_line = s.readline()
        if len(sw_line) == 0:
            break
        stop_words.append(sw_line.split())

stop_words = [s_item for s_sublist in stop_words for s_item in s_sublist]
set_stop = {i_s.lower() for i_s in stop_words}

with open('shakespeare.txt', mode='r', encoding='utf-8') as w:
    # with open('data/mini98.txt', mode='r') as w:
    while True:
        cline = w.readline()
        if len(cline) == 0:
            break
#        cline = re.sub(r'[^a-zA-Z0-9 \']', '', string=cline).lower().strip().rstrip().replace('\n', '')
        cline = re.sub(r'[^a-zA-Z0-9 \']', '', string=cline).lower()
        words.append(cline.split())

all_words = [w_item for w_sublist in words for w_item in w_sublist]
set_all = {i_w for i_w in all_words}

excl_words = set_all.intersection(set_stop)
excl_words_List = list(excl_words)
def_words = selecting_words(excl_words_List, all_words)

word_stats = collections.Counter(def_words).most_common(10)
for i in word_stats:
    print(i[0], ':', i[1])
