# coding = utf-8
import  json
import  requests
import  codecs
import  logging

'''
 *  @author shengli881026@163.com
'''

logging.debug("ssssss")
logging.info(u"麻生希")


'''
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Start print log")
'''



'''
 *  抓取掘金<juejin.im>网站的 - 相亲模块的数据
 * 
 * 网站地址:
 * https://short-msg-ms.juejin.im/v1/pinList/topic?uid=&device_id=&token=&src=web&topicId=5abcaa67092dcb4620ca335c&page=2&pageSize=20&sortType=rank
 *  @author zhangshengli@163.com 
'''
class JmData :

    url = "https://short-msg-ms.juejin.im/v1/pinList/topic?uid=&device_id=&token=&src=web&topicId=5abcaa67092dcb4620ca335c&page={page}&pageSize={page_size}&sortType=rank"
    '''
     * 初始化模块
     * 初始化抓取的页数,还有抓取的每页列表数；
     * 
    '''
    def __init__(self,page = 0,page_size = 20):
        self.page = page
        self.page_size = page_size
        self.request = requests
        self.url = self.url.format(page = page,page_size = page_size)
        print("................爬虫已准备就绪,开始爬取 url : " + self.url + "的内容................",'\n')

    def GetParams(self):
        return [self.page,self.page_size,self.url]

    '''
     * GetData 抓取数据接口，获取Url 的Json 数据接口，通过requests Post请求获取
     * 获取成功后return data;
    '''
    def GetData(self,page):
        ret = self.request.get(url = self.url)
        result = json.loads(ret.content.decode())
        if (result['m'] == 'success'):
            print("一共采集到"+format(result['d']['total'])+'条数据')


        self.LogInfo()
        return result['d']['list']
    '''
     * 格式化数据的接口，用于对Url请求的结果进行格式化处理，返回对应的数据；
     * @return data;
    '''
    def FormatData(self):
        pass

    '''
     * 记录采集数据的日志，用于清楚采集的过程和结果；
     * log_level [1:'debug',2:'info',3:'warning',4:'error',5:'critical']
     * @ logging 模块的使用
    '''
    def LogInfo(self,log_level = 0):
        level_dit = {0:'debug',1:'info',2:'warning',3:'error',4:'critical'}
        level_str = level_dit[0]
        #print(level_str)
        #logging.debug("oeowoksksks skssk")
        #logging.level[]("ssss")
        pass


        


jm_obj = JmData(page=0,page_size=20)
print(jm_obj.GetData(2))
def strAbc():
    pass
#print(jm_obj.__dict__)
#print(JmData.__dict__)
#csdn_obj.GetData(1)
#print(csdn_obj.GetParams())
