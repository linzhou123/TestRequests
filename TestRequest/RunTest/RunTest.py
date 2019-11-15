from Base.HTMLTestRunner import HTMLTestRunner
import os,time,unittest

dirpath = os.path.dirname(os.path.dirname(__file__))

casepath = os.path.join(dirpath,"TestCase")
reportName="report"+time.strftime("%Y_%m_%d")+".html"
reportpath=os.path.join(dirpath,'CaseResult',reportName)
# print(reportpath)
all_cases=unittest.defaultTestLoader.discover(casepath,pattern='test*.py')

print(all_cases)
# runner = unittest.TextTestRunner()

fp = open(reportpath,'wb')
runner = HTMLTestRunner(stream=fp,
                        title='Tpson接口自动化测试报告',
                        description='Tpson接口自动化测试报告',
                        )

runner.run(all_cases)