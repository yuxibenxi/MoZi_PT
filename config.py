# -*- coding: utf-8 -*-
"""
@author: Chen Weiling
@software: PyCharm
@file: config_example.py.py
@time: 3/23/2020 11:33 AM
@comments: 
"""

import os
import torch



# 默认单词标记
PAD_token = 0  # 用于填充短句
SOS_token = 1  # 句头标记
EOS_token = 2  # 句尾标记
Unk_token = 3  # 未知标记
MAX_LENGTH = 64  # 要考虑的最大句子长度
MIN_COUNT = 3  # 修剪的最小字数阈值


# 模型参数
model_name = 'mozi_model'
attn_model = 'dot'
#attn_model = 'general'
#attn_model = 'concat'
hidden_size = 300  # embedding维数，此时使用fasttext维数即300
encoder_n_layers = 4 # 编码器层数
decoder_n_layers = 4 # 译码器层数


# Configure training/optimization
clip = 20.0 # 批？
teacher_forcing_ratio = 1.0 # 教习比 0.0 - 1.0
decoder_learning_ratio = 1.0 #编码器学习比
n_iteration = 100000  # epoch，训练次数
learning_rate = 1e-3 # 学习率
dropout = 0.0 # 正则化
batch_size = 200 # 批
min_loss = 0.0

print_every = 1
save_every = 500

# 运行时参数
lang = "cn"  # cn为中文，填写其他则默认为英文
corpus_name = "mozi"
# corpus_name = "cornell movie-dialogs corpus"
checkpoint_iter = None  # 上次保存模型时的训练步数
loadFilename = None  # 初始训练时设置为None
"""
loadFilename = os.path.join('data/save', model_name, corpus_name,
                             '{}-{}_{}'.format(encoder_n_layers, decoder_n_layers, hidden_size),
                             'checkpoint.tar')
#"""
fastTextEmb = os.path.join('data/embedding', 'wiki.zh.vec')  # fastText embedding 文件地址
fastTextGensim = os.path.join('data/embedding', 'gensim_fasttext.mod')  # gensim加载fasttext后的模型
embeddingFile = os.path.join('data', 'embedding_bq.pkl')  # 从fastText的embedding中过滤处理过要用的embedding文件
sentEmbFile  = os.path.join('data', 'sent_emb.pkl')  # 存储计算好的句子向量文件
vocFile = os.path.join('data', 'voc_bq.pkl')
pairsFile = os.path.join('data', 'pairs_bq.pkl')
dialogFile = os.path.join('data', 'mozi3.tsv')
annoyIdxFile = os.path.join('data', 'sent_emb_idx.ann')
ballTreeIdxFile = os.path.join('data', 'sent_imb_idx.tre')
mode = "train"
debug_gen = False  # 是否开启生成模型的debug模式
debug_ret = False  # 是否开启检索模型的debug模式
debug_hyb = True  # 是否开启混合模型的debug模式
retrieve_mode = "ball_tree"  # 支持["annoy", "brute_force", "ball_tree"]
threshold_ret = 0.9965  # brute force 检索模型相似度阈值，越大越相似
threshold_ann = 0.0836  # annoy index 检索模型相似度阈值，越小越相似, math.sqrt(2-2*threshold_ret)
threshold_tree = 0.9164  # ball tree 检索模型相似度阈值，有待调参
masked = False  # 选择计算loss是是否考虑mask



if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
    torch.set_num_threads(16)

