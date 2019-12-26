import json
import re

source_string = """<p>a_10_{s_19_"Email_1537964292843":s_17_"test@example.com":s_18_"Name_1537964408919":s_27_"Сердюченко А.В.":s_20_"Number_1537965108659":s_11_"89266546565":s_20_"Number_1537964605246":s_14_"34234234234234":s_20_"Select_1554716151062":s_46_"Телекоммуникации и связь":s_20_"Select_1537961382465":s_16_"Директор":s_20_"Select_1554716446038":s_44_"Улучшить поиск тендеров":s_19_"Radio_1537966439272":s_27_"Сайт":s_18_"Date_1554715944286":s_10_"14-10-2019":s_21_"Message_1554715551345":s_22_"Комментарий":}</p>NULL"""

items = re.findall(r'{.+?}', source_string)
for item in items:
    fields = re.findall(r'".+?"', item)
    pattern = re.compile('^"|"$')
    fields = list(map(lambda x: pattern.sub("", x), fields))
    dict_item = {}
    for (i, field) in enumerate(fields):
        if i % 2 != 0:
            continue
        dict_item[field] = fields[i+1]
    print(json.dumps(dict_item, ensure_ascii=False))

