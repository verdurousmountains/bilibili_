import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import PlaintextCorpusReader
from nltk.classify import accuracy as nltk_accuracy
def massage_feature(word,num_letter=1):return {'feature':word[-num_letter:]}
def bayessss(test_file,train_file,test_lable,train_lable,number_test):
    message_corpus = PlaintextCorpusReader('./', [test_file, train_file])
    labels_name = ([(massage, test_lable) for massage in message_corpus.words(test_file)] +
                   [(massage, train_lable) for massage in message_corpus.words(train_file)])
    featuresets = [(massage_feature(n), massage) for (n, massage) in labels_name]
    train_set, test_set = featuresets[number_test:], featuresets[:number_test]
    classifier = NaiveBayesClassifier.train(train_set)
    p1=100*nltk_accuracy(classifier,test_set)
    print('结果准确率：',str(p1)+str('%'))
for zz in [50,100,200,300,400,500,1000,2000]:
    for j in [r'G:\my_sao_xm\jieba_after\0动画.txt',r'G:\my_sao_xm\jieba_after\1鬼畜.txt',
                r'G:\my_sao_xm\jieba_after\2国创.txt',r'G:\my_sao_xm\jieba_after\3科技.txt',
                r'G:\my_sao_xm\jieba_after\4生活.txt',r'G:\my_sao_xm\jieba_after\5时尚.txt',
                r'G:\my_sao_xm\jieba_after\6舞蹈.txt',r'G:\my_sao_xm\jieba_after\7音乐.txt',
                r'G:\my_sao_xm\jieba_after\8影视.txt',r'G:\my_sao_xm\jieba_after\9游戏.txt',
                r'G:\my_sao_xm\jieba_after\10娱乐.txt']:
        for i in [r'G:\my_sao_xm\jieba_after\0动画.txt',r'G:\my_sao_xm\jieba_after\1鬼畜.txt',
                r'G:\my_sao_xm\jieba_after\2国创.txt',r'G:\my_sao_xm\jieba_after\3科技.txt',
                r'G:\my_sao_xm\jieba_after\4生活.txt',r'G:\my_sao_xm\jieba_after\5时尚.txt',
                r'G:\my_sao_xm\jieba_after\6舞蹈.txt',r'G:\my_sao_xm\jieba_after\7音乐.txt',
                r'G:\my_sao_xm\jieba_after\8影视.txt',r'G:\my_sao_xm\jieba_after\9游戏.txt',
                r'G:\my_sao_xm\jieba_after\10娱乐.txt']:
            bayessss(j,i,'yes','no',zz)
        print('测完一个开始下一个')
    print('修改测试集样本数')