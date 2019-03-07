import pandas as pd
data = pd.read_excel(r"G:\my_sao_xm\danmu\3keji.xls",encoding='utf-8',sep='	',header=None)
import jieba
data[1]=data[1].map(lambda x:' '.join(jieba.cut(x)))
data.to_csv('3科技.csv',encoding='utf-8',header=False,index=False,columns=[1])