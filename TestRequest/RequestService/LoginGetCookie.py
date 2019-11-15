from Base.HttpBase import HttpBase
from Base.ReadExcel import Read_Excel
import os
from Base import Log,GetYamlFile
log=Log.Log()
#获取登录的cookie
def getCookie():
    YmlList=GetYamlFile.getYamlFile()
    TestCasePath=YmlList["TestCasePath"]
    TestDomainName=YmlList["TestDomainName"]
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    REPORT_XLSX_DIR = os.path.join(PROJECT_ROOT, TestCasePath)
    readBook=Read_Excel(REPORT_XLSX_DIR)
    DomainUrl=readBook.read_Excel(TestDomainName,1,0)
    GetCookieInterface=readBook.read_Excel(TestDomainName,1,1)
    url=DomainUrl+GetCookieInterface
    # data={'username':'admin','password':'password'}
    data=readBook.read_Excel(TestDomainName,1,2)
    data=eval(data)
    cookie=HttpBase(url,data,"post",None).getHttpHeaders().get("Set-Cookie")
    # print(cookie)
    log.info("得到cookie："+cookie)
    return cookie


if __name__=='__main__':
    x=getCookie()
