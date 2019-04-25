import os
import re

file1 = open("innerinterfaces.txt","r")
str1 = file1.read()
keys = re.findall(r'(^[0-9]+\.)', str1, re.M)
# 正则就是字符串处理,"\n"被当成了字符(ASCII值为"5C 6E"),“\n2.”就无法识别为“以2.开头”，所以去掉“r'(^[0-9]+\.)'”中的“^”.
# 正则是否带r，也有区别。有r会保留匹配的项，没有r去掉匹配的项。所以去掉“r'([0-9]+\.)'”中的“r”
jsons = re.split('[0-9]+\.', str1)
# 去掉list中的第一个空对象
# utf8格式中，汉字为3个ASCII字符。去掉所有的空格(ASCII值为20)和tab键(ASCII值为09)，tab一般会变成多个空格。
# 将“：”替换为“:”
# 去掉\n
#
jsons.pop(0)

