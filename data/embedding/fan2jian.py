import opencc

import fasttext
import fasttext.util

ft = fasttext.load_model ('wiki.zh.bin')
ft.get_dimension()
fasttext.util.reduce_model(ft, 192)
ft.get_dimension()



'''
cc = opencc.OpenCC('t2s')

input = open("wiki.zh.vec","r")
output = open("zh.vec","w")

a=0
for l in input.readlines():
    a+=1
    output.write(cc.convert(l)+"\n")

print(a)
'''
