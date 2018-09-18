
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


filepath = r'D:\data\wiki_cn'


# In[3]:


f = open(filepath,'r',encoding='utf-8',errors='ignore')


# In[4]:

# In[5]:

lines = []

# # 获得本文

# In[6]:

for i in f.readlines():
    if len(i)>10:
        lines.append(i.strip())

# In[7]:

len(lines)

# In[9]:


# lines[1]


# In[12]:


len(lines[1])


# In[10]:


del(f)


# # 从文本提取关键词

# In[8]:


from jieba import analyse
tfidf = analyse.extract_tags


# ## 使用*TF-IDF* 提取关键词

# In[11]:


keywords = []


# In[15]:


for i in lines:
    keyword = tfidf(i)
    if len(keyword)>8:
        keyword = keyword[:8]
    keywords.append(keyword)


# In[16]:


len(keywords)


# In[17]:


keywords[:4]


# In[18]:


lines[3]


# ## 使用*Textrank* 提取关键词

# In[9]:


keywords = []
max_len = 8


# In[11]:


for i in lines:
    keyword = analyse.textrank(i)
    if len(keyword) > max_len:
        keyword = keyword[:max_len]
    keywords.append(keyword)


# In[12]:


len(keywords)


# In[15]:


keywords


# In[16]:


keywords[3]


# # 建立*token* 字典

# In[13]:


from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer


# In[14]:


token = Tokenizer(num_words=8000)


# In[15]:


token.fit_on_texts(keywords)


# In[16]:


token.word_index


# # lines分词

# In[17]:


import jieba


# In[18]:


jieba.load_userdict(token.word_index)


# In[19]:


text_jieba = []


# In[20]:


for i in lines:
    text_jieba.append(list(jieba.cut(i))) #print(','.join(seg_list))
    


# In[33]:


lines[0]


# In[36]:


list(jieba.cut(lines[0]))


# In[41]:


len(text_jieba[0])


# # 使用sklearn库的*train_test_split* 分离训练测试集

# In[ ]:


from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test = train_test_split(text_jieba,keywords,test_size=0.4, random_state=0)


# In[ ]:


len(x_train),len(x_test),len(y_train),len(y_test)


# # 将文字转换为数字列表

# In[43]:


x_train_seq = token.texts_to_sequences(x_train)
x_test_seq = token.texts_to_sequences(x_test)
y_train_seq = token.texts_to_sequences(y_train)
y_test_seq = token.texts_to_sequences(y_test)


# In[44]:


x_train_seq[:3]


# In[45]:


x_train[:3]


# # 规范长度

# In[ ]:


x_train = sequence.pad_sequences(x_train_seq,maxlen=8)
x_test = sequence.pad_sequences(x_test_seq,maxlen=8)
y_train = sequence.pad_sequences(y_train_seq,maxlen=200)
y_test = sequence.pad_sequences(y_test_seq,maxlen=200)


# # 建立模型
# + 嵌入层 *将数字转换为向量*
# + Dropout(0.2)
# + RNN层 units=128
# + RNN层 units=64
# + 隐藏层 units=256,activation='relu'
# + Dropout(0.35)
# + 输出层 units=200,activation='sigmoid'

# In[ ]:


from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import SimpleRNN


# In[ ]:


model = Sequential()


# In[ ]:


model.add(Embedding(output_dim=64,
                   input_dim=8000,
                   input_length=8))
model.add(Dropout(0.35))


# In[ ]:


model.add(SimpleRNN(units=128))


# In[ ]:


model.add(SimpleRNN(units=64))


# In[ ]:


model.add(Dense(units=256,activation='relu'))
model.add(Dropout(0.35))


# In[ ]:


model.add(Dense(units=200,activation='sigmoid'))


# In[ ]:


model.summary()


# # 训练模型

# In[ ]:


model.compile(loss='binary_crossentropy',
             optimizer='adam',
             metrics=['accuracy'])


# In[ ]:


train_history = model.fit(x_train,y_train,
                         batch_size=10000,
                         epochs=10,
                         verbose=2,
                         validation_split=0.2)


# # 显示训练过程

# In[ ]:


import matplotlib.pyplot as plt
def show_train_history(train_history,train,validaiton):
    plt.plot(train_history.history[train])
    plt.plot(trian_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train','validation'])
    plt.show()


# In[ ]:


show_train_history(train_history,'acc','val_acc')


# # 评估模型准确率

# In[ ]:


scores = model.evaluate(x_test,y_test,verbose=1)


# # 进行预测

# In[ ]:


predict = model.predict(x_test)


# # 保存模型

# In[ ]:


from keras.models import load_model


# In[ ]:


model.save('version.h5')


# # 加载模型

# In[ ]:


model.load_model('version.h5')

