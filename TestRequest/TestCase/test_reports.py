#-*-coding:utf-8-*-
from RequestService.ExcelRequest import getAllCase,TestGo,WriteResult

import ddt
import unittest

caseList=getAllCase()
@ddt.ddt
class Test(unittest.TestCase):
    '''ddt形式执行用例 用例使用caseList'''
    @ddt.data(*caseList)
    def test_requests(self,data):
        result=TestGo(data)
        WriteResult(result)
        self.assertTrue(data["hopeResult"] in result["actualResult"])
if __name__=='__main__':
    unittest.main()