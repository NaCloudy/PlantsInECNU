import pandas as pd
import jieba
import jieba.analyse

from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt

from wordcloud import WordCloud

# 读取文件
pd_data = pd.read_excel('D:/ECNU/23_2spring/cs-DataVisualization/miniproject/wordcut/text_to_be_cut.xlsx',engine='openpyxl')
# 删除空行
exist_col = pd_data.dropna()
# 读取内容
text = exist_col['校友寄语'].astype(str).tolist()
text=[i.replace('_x000D_','\r') for i in text]
# 切割分词,精确模式
wordlist = jieba.lcut(''.join(text))
result =' '.join(wordlist)
ciyun_words = result

# 遮罩图片 
img = Image.open("D:/ECNU/23_2spring/cs-DataVisualization/miniproject/wordcut/cloud.png") # 打开遮罩图片 
mask = np.array(img) #将图片转换为数组

# 设置停用词
stop_words = ['的','了','和','有','与',
              '不','着','过','在','从',
              '中','是','从','就','都',
              '为','到','还','说','也',
              '并','来','那','后','于',
              '以','上','之','这','会',
              '而','最','地','又','去',
              '把','等','你','我','里',
              '人','它','下','被','及',
              '一','成',]

# 权重分析
tag = jieba.analyse.extract_tags(sentence=ciyun_words, topK=150, withWeight=True)
# 符合json格式
new_data = ' '.join([d[0] for d in tag]) 
print(new_data) 
# 手动删去了new_data中的人名然后粘贴过来
mywords = "我们 母校 华师大 师大 同学 华东师大 校友 青春 华东师范大学 上海 毕业 校园 学生 人生 老师 成长 学习 感恩 学子 管理 学校 丽娃 创业 经济系 感谢 经济学 河畔 金融 美好 水杉 时光 学院 岁月 四年 10 70 MBA 自己 工作 捐赠 一起 成为 20 30 美丽 大家 导师 班级 大学 一个 未来 相聚 丽娃河 英文 祝愿 专业 祝福 时代 发展 这里 情怀 中国 希望 社会 记忆 华师 2016 收获 桃李 教室 不断 教育 校门 度过 投资 企业 设计 建设 来自 行业 世界 就是 长青 特色 师恩 一年 在丽娃 2019 1992 记得 回忆 活动 硕士 一次 理想 精神 少年 梦想 他们 时候 见证 因为 五湖四海 辉煌 幸福 生活 忘不了 这棵树 1987 50 庄泰 12 作为 四载 陪伴 归来 周年 领域 三十年 一生 来 到 事业 难忘 百年树人 代表 经历 创新 教授 彼此 自律 资本 多年 期间 公司 有人 这棵 先后 知识 服务 大夏 经营 无论 获得 一位 路上 传承 国际"

# 词云生成
wc = WordCloud(font_path="msyh.ttc",   #直接对所有单词进行词云生成             
               mask=mask,                
               width = 1650,                
               height = 950, 
               min_font_size = 15,
               prefer_horizontal = 0.95,               
               background_color='white',                
               max_words=200,
               relative_scaling = 0.7,                
               stopwords=stop_words,
               colormap = 'summer',
               ).generate(ciyun_words)
wc2 = WordCloud(font_path="msyh.ttc",   #对权重最高的150个词进行词云生成                             
               mask=mask,                                
               width = 1650,                                
               height = 950,                 
               ## min_font_size = 35,                
               prefer_horizontal = 0.9,                               
               background_color='white',                                
               max_words=200,                
               ## relative_scaling = 0.6,                                
               ## stopwords=stop_words,                
               colormap = 'summer',                
               ).generate(mywords)

# 显示词云 
# 用plt显示图片 
plt.imshow(wc, interpolation='bilinear')
# 不显示坐标轴 
plt.axis("off")
# 显示图片  
plt.show() 
# 保存到文件 
wc.to_file("D:/ECNU/23_2spring/cs-DataVisualization/miniproject/wordcut/all_words.png")
wc2.to_file("D:/ECNU/23_2spring/cs-DataVisualization/miniproject/wordcut/top150_words.png")