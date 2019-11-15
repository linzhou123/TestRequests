from Base.ReadExcel import Read_Excel
from Base.HttpBase import HttpBase
from Base.WriteExcel import Write_excel
from RequestService.LoginGetCookie import getCookie
import os,time
from Base import Log,GetYamlFile
log=Log.Log()
def getAllCase():
    num=2
    list=[]
    YmlList=GetYamlFile.getYamlFile()
    TestCasePath=YmlList["TestCasePath"]
    TestDomainName=YmlList["TestDomainName"]
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    REPORT_XLSX_DIR = os.path.join(PROJECT_ROOT, TestCasePath)
    readBook=Read_Excel(REPORT_XLSX_DIR)
    url=readBook.read_Excel(TestDomainName,1,0)
    for sheetNames in readBook.get_SheetName():
            #过滤域名TestDomainName
            if sheetNames !=TestDomainName:
                allNum=readBook.get_RowNums(sheetNames)
                for itemNum in range(1,allNum):
                    # print(readBook.read_Excel("Request",itemNum,0))
                    #获取测试名称
                    testName=readBook.read_Excel(sheetNames,itemNum,0)
                    #获取请求方式
                    method=readBook.read_Excel(sheetNames,itemNum,1)
                    #获取url
                    url2=readBook.read_Excel(sheetNames,itemNum,2)
                    #获取参数
                    params=readBook.read_Excel(sheetNames,itemNum,3)
                    if params.strip()=='':
                        log.info(testName+"：该用例参数为空")
                    else:
                        params=eval(params)
                    #获取预期结果
                    hopeResult=readBook.read_Excel(sheetNames,itemNum,4)
                    #拼接完整的url
                    urlAll=url+url2
                    #用字典形式读取单个case
                    excelData={
                        "rowNum":num,
                        "testName":testName,
                        "method":method,
                        "url":urlAll,
                        "params":params,
                        "hopeResult":hopeResult
                    }
                    num+=1
                    #用数组形式写入所有case
                    list.append(excelData)
    log.info(list)
    return list

def TestGo(case):
    result={}
    #返回cookie
    cookie=getCookie()
    headers={
        "cookie":cookie
    }
    #写入自定义返回结果
    request=HttpBase(case["url"],case["params"],case["method"],headers).RequestRun()
    #写入row数字
    result["rowNum"]=case["rowNum"]
    #写入测试用例名称
    result["testName"]=case["testName"]
    #写入请求方式
    result["method"]=case["method"]
    #写入完成的rul
    result["url"]=case["url"]
    #写入参数
    result["params"]=case["params"]
    #写入预期结果
    result["hopeResult"]=case["hopeResult"]
    #写入实际结果
    result["actualResult"]=str(request.content,'utf8')
    #写入接口运行时间
    result["time"]=str(request.elapsed.total_seconds())
    #判断实际结果是否包含预期结果内容，且输出结果 pass or fail
    if result["hopeResult"] in result["actualResult"]:
        result["result"]="pass"
        log.info(result["testName"]+"测试结果正常")
    else:
        result["result"]="fail"
        log.info(result["testName"]+"响应内容不匹配")
    get_result=str(result)
    log.info("获取测试结果:"+get_result)
    return result
"""
写入报告（Excel形式）
"""
def WriteResult(result):
    YmlList=GetYamlFile.getYamlFile()
    CaseResultPath=YmlList["CaseResultPath"]
    today=time.strftime("%Y_%m_%d")
    CaseResultPath=CaseResultPath+"\Result"+today+".xlsx"
    #获取项目路径
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    #join 拼接具体路径
    REPORT_XLSX_DIR = os.path.join(PROJECT_ROOT, CaseResultPath)
    rowNum=result["rowNum"]
    wt = Write_excel(REPORT_XLSX_DIR,"Result")
    wt.write(1,1,"用例名称")
    wt.write(1,2,"请求方式")
    wt.write(1,3,"URL")
    wt.write(1,4,"params")
    wt.write(1,5,"hopeResult")
    wt.write(1,6,"actualResult")
    wt.write(1,7,"是否通过")
    wt.write(1,8,"运行时间")
    wt.write(rowNum,1,result["url"])
    wt.write(rowNum,2,result["method"])
    wt.write(rowNum,3,result["url"])
    wt.write(rowNum,4,result["params"])
    wt.write(rowNum,5,result["hopeResult"])
    wt.write(rowNum,6,result["actualResult"])
    wt.write(rowNum,7,result["result"])
    wt.write(rowNum,8,result["time"])

if __name__=='__main__':
    # RequestGo()
    getAllCase()