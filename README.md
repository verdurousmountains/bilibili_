# zhouzhenyu
- 上学期统计推断这门课的案例展示。 
- 想法来源于基于调用nltk朴素贝叶斯的垃圾短信分类，随手试了下b站视频弹幕分类（区）。
- 整个过程包括爬虫、数据预处理、分类测试。本以为挺简单的，数据预处理比我想象的要麻烦的多。
- 1.在b站排行榜榜单中各区选取月（30）热度前100的视频，爬取弹幕。2.弹幕处理（格式转换、乱序、分词）3.分类
- jieba_after文件是最初的数据集，虽然各区爬取视频数量大致相同，但弹幕总数有较大差异。后对原始数据集进行删减，控制各区数据数量基本保持一致。
- 数据集有限，结果是理所当然的失败了23333，比瞎蒙稍微好一点点，不过还是非常有收获的~
