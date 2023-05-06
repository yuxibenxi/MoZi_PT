import random
import re

def clrpoint(sentence):
    sentenceClean = []
    # method 1 ，～、：＃；％＊——……＆·￥（）‘’“”[]『』〔〕｛｝【】‖〖〗《》「」｜〈〉«»‹›.@~-,:*?!_#/=+﹉&^;%…$()\..<<|·¥[]"{}–'€¡¿`´＂＇£¢฿♀♂>）
    remove_chars = '[·’"\#$%&\'()＃（）*+-./:;<=>\@：￥★』『、…．＞【】［］《》“”‘’\[\\]^_`{|}]+'
    string1 = re.sub(remove_chars, "", sentence)
    sentenceClean.append(string1)
    return "".join(sentenceClean).replace("   "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")


out_file = open('mozi2.random.tsv', 'w', encoding='utf-8')  # 输出文件位置

lines = []

with open('mozi2.tsv', 'r', encoding='utf-8') as f:  # 需要打乱的原文件位置
    for line in f:
        lines.append(line)

random.shuffle(lines)

for line in lines:
    out_file.write(clrpoint(line))

out_file.close()
