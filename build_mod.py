import pickle
from config import *
from gensim.models import KeyedVectors
# 因为通过gensim来load fasttext预训练的词向量速度非常慢，所以这里先load一次之后保存成pickle，之后读取pickle速度会快一些
model = KeyedVectors.load_word2vec_format(fastTextEmb)
with open(fastTextGensim, 'wb') as f:
    pickle.dump(model, f)

