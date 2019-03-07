import requests
from lxml import etree
import re
from pprint import pprint
import json

class Bili(object):
    def __init__(self,url_num):
        self.name = "av号"+str(url_num)
        self.url = "https://www.bilibili.com/video/av{}".format(url_num)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
        }

    def parse(self, url):
        response = requests.get(url,headers=self.headers)
        res = response.content.decode()
        return res

    def get_content(self,res):
        html = etree.HTML(res)
        item = {}
        item["title"] = html.xpath("//div[@id='viewbox_report']/h1/@title")[0] if len(html.xpath("//div[@id='viewbox_report']/h1/@title"))>0 else None
        if item["title"]:
            item["cid"] = re.findall(r"cid=([\d]+)&amp;",res)[0]
        else:
            return None
        print(item)
        return item

    def get_url(self, item):
        cid = item["cid"]
        danmu_url = "https://comment.bilibili.com/{}.xml".format(cid)
        print(danmu_url)
        return danmu_url

    def get_danmu(self, res, item):
        # pprint(res)
        html = etree.HTML(res.encode())
        item["弹幕"] = html.xpath("//d/text()")
        # pprint(item)
        return item

    def save(self, name, content):
        with open(r"F:\my sao xm\影视\{}.json".format(name),"a",encoding="utf-8")as f:
            f.write(json.dumps(content,ensure_ascii=False,indent=4))
            print("保存成功")

    def run(self):
        item = {}
        # 1 获取url
        # 2 发送请求，获取相应
        res = self.parse(self.url)
        # 3 提取cid和标题
        item = self.get_content(res)
        if item==None:
            print("vid号不正确，请重新输入。")
            return
        # 4 组合弹幕url
        danmu_url = self.get_url(item)
        # 5 发送请求获取相应
        res_danmu = self.parse(danmu_url)
        # 6 提取
        end = self.get_danmu(res_danmu, item)
        # 7 保存
        self.save(self.name,end)
        print("程序结束")
for i in [35861132,35178088,35097776,35533905,34513490,34897078,35658723,35116015,35575194,35863472,35621641,35027096,34162079,35731753,35750923,35986202,35326207,35634690,34524225,34562343,34889975,35377122,36331554,35834078,36829653,34708900,35690179,34963415,36197600,35177390,35482618,34731982,35671888,34811773,35332962,34697472,34887154,36065787,34997660,35266951,36107219,35914181,35146762,36015710,34719395,35668885,35667837,36096580,35545829,34518858,35028727,34591954,35595616,35025586,34625438,35517954,34558200,34803020,34725668,35689538,34466422,35620858,35021381,36050193,36054426,35103609,36555357,35588534,35966452,34408726,35818816,34355469,35900519,36619109,36479436,35697487,34858816,31459785,34810104,34589050,35100412,35336015,35934928,35613192,35657153,34911712,36575468,34163567,35547221,34878064,33792455,33743839,35604595,35283035,35476884,35872928,35993025,36146180,34513606,35437370,34818622,35805965,32909376,35341303,34869618,35896513,35506694,33305444,35079102,36607967,35899654,34635425,36217861,35483258,35130352,34329227,35520007,34921002,35951528,34077575,36028771,35231172,35902240,34098516,34624308,34066401,35328259,36406443,34393996,35073135,34819619,34941112,35661275,33537821,35856650,35635830,35689362
          ]:
    if __name__ == '__main__':
        url_num = i
        b = Bili(url_num)
        b.run()
