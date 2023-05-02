[一个姑且算是聊天机器人的教程](https://www.jianshu.com/p/e7bf16d7a33a)放了一些比较琐碎不适合放在`README`里的内容。

# Requirements
   git clone -v https://github.com/yuxibenxi/MoZi_PT.git
   cd MoZi_PT
   pip3 install -r requirements.txt
# 数据相关
## 训练语料
声明：
暂时不方便提供我自己收集的语料(太大惹)，建议可尝试使用小黄鸡的语料。

格式：  
问题\t回答 （一个pair占一行，**句子均已用jieba分词**）

例子：  
出 任务 又 受伤 了 ？	不 碍事 的 ， 只是 小伤 罢了 。  
新年快乐	新年快乐 ， 这 不是 祝福 ， 是 承诺 。  
你 通宵 了 ？	昨晚 在 出 任务 。 抱歉 ， 让 你 担心 了 。

数据量参考：  
对话11000000，词汇让我看看啊，训练次数100000+  

存放路径：  
使用`config.py`的变量`dialogFile`指定对话存放路径

## 预训练词向量
推荐使用fastText使用维基百科训练的词向量，[下载地址](https://fasttext.cc/docs/en/pretrained-vectors.html)

# 运行方法
## 生成模型
生成模型参考了pytorch的chatbot教程，主要是seq2seq模型+attention。
### 训练模型
1. 运行`python3 generate_voc_pairs.py`生成词汇表和问答pairs
2. 运行`python3 preprocess_emb.py`预处理预训练的词向量（如果不需要预训练词向量可跳过此步骤，`config.py`中设置`embeddingFile`为`None`即可）
3. 在`config.py`文件中配置相关参数（参考`config_example.py`）
 - 设置`mode="train"`
 - 首次训练设置`loadFilename=None`，如果是接着训练则设置`checkpoint_iter`为上次训练的次数，并设置`loadFilename`为存档地址
4. 运行`python3 train.py`训练模型，训练完后可与机器人对话，输入quit结束
 - 如果训练集噪音太大loss一直波动的话可以一直减小学习率，比如1e-7

### 测试模型
1. 在`config.py`文件中配置相关参数
 - 设置`mode="evaluate"`
 - 设置`checkpoint_iter`为上次训练的次数，并设置`loadFilename`为存档地址
2. 运行`python3 train.py`训练模型，可与机器人对话，输入quit结束

## 检索模型
检索模型主要就是将句子表示成向量后，搜索最近邻（KNN）。实现的三个不同的模型主要在速度和准确性上稍有区别。
1. 运行`python3 compute_sent_emb.py`完成检索模型所需要的准备工作：  
将`gensim`加载`fastText`词向量后得到的模型存储在路径`fastTextGensim`下，具体参考[这里](https://github.com/coranholmes/pt_chatbot/issues/2)  
计算知识库中所有句子的句向量保存`sentEmbFile`  
创建annoy index备查  
创建ball tree对象备查  
2. `config.py`中的`retrieve_mode`支持`brute_force`, `annoy`和`ball_tree`三种方式，设置需要的检索模型后运行`retrieval.py`。其中brute force速度比较慢，但是准确性有保证，annoy速度最快，数据量级上去了也没问题，但是结果可能比brute force稍差，不过我目测了基本差不多。
3. 运行`python3 retrieval.py`，可与机器人对话，输入quit结束

## 混合模型
混合模型综合了生成模型和检索模型的结果，当检索模型召回的answer与用户输入的query相似度不满足阈值条件则进一步调用生成模型返回结果。前两个模型都跑通的话可以用如下方法运行混合模型：
1. 运行`python3 hybrid_model.py`，可与机器人对话，输入quit结束

## Web API
1. 用POST

# 训练效果
## 混合模型
bot的训练语料全是谈情说爱性质的，这方面的回答就比较好，而比较新的话题例如金融危机、covid-19等则会容易文不对题。  
<img src="./imgs/测试.png" width=300>  

# 未来工作
1. 优化
2. 打算公开训练集

# 参考
http://fancyerii.github.io/2019/02/14/chatbot/  
https://github.com/llSourcell/tensorflow_chatbot

# 改进
1. 添加用来打底的检索模型
2. 支持对话中出现单词表中不包含的单词
3. 支持载入预训练的词向量
4. 支持中文会话
5. 更改loss function

# 相对于主分支
1. 加入一些工具
2. 能更好的在现在的软件环境运行
3. 删除GUI
4. 出现异常会直接停止训练
5. 更改loss function

# 扩展
用相同的语料微调了中文GPT模型，虽然数据不能分享，但是模型可以分享啊！build成docker image了，戳[这里](https://hub.docker.com/r/coranholmes/cdial-gpt)来一场甜甜的恋爱吧\(^o^)/~肉眼看一下这个GPT模型还是比之前的seq2seq+attn的模型效果要好很多。
