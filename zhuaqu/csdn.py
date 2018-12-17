# coding = utf-8
import  json
import  requests
import  codecs

'''
 *  抓取CSDN相关的关键词内容数据
 * 
 *  @author zhangshengli@163.com 
'''
class CsdnData :

    def __init__(self):
        pass

    def GetData(self,page):
        print("page : " + str(page))
        pass



csdn_obj = CsdnData()
csdn_obj.GetData(1)
