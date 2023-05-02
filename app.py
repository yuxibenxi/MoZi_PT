# -*- coding: utf-8 -*-
"""
@author: Chen Weiling
@software: PyCharm
@file: app.py.py
@time: 3/23/2020 1:59 PM
@comments: 
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pickle
from model import *
# from utils import *
from flask import Flask, request
from flask import jsonify


import re

zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def reply():
    req_msg = request.form['msg']
    """
    print('Message received:', req_msg)
    res_msg, sim = retrieveAnswer_ann(req_msg, sent_emb, u)
    if sim > threshold_ann:
        res_msg = generateAnswer(req_msg, searcher, voc)
    """

    res_msg = generateAnswer(req_msg, searcher, voc)
    print('Message sent:', res_msg)
    # 如果接受到的内容为空，则给出相应的回复
    if res_msg.isspace():
        res_msg = '喵喵喵？'

    return jsonify({'text': res_msg})


# 启动APP
if (__name__ == "__main__"):
    encoder, decoder, voc, pairs, embedding, checkpoint = initGenModel()

    # Set dropout layers to eval mode
    encoder.eval()
    decoder.eval()

    # Initialize search module
    searcher = GreedySearchDecoder(encoder, decoder)
    #sent_emb = pd.read_pickle(sentEmbFile)
    
    
    # 结巴分词准备
    init = "".join(list(jieba.cut("结巴分词初始化")))

    # 加载annoy index
    """
    u = AnnoyIndex(hidden_size, 'angular')
    u.load(annoyIdxFile)
    """

    # 启动APP
    app.run(host='0.0.0.0', port=8088)
