import xlrd
import os
from Base import GetYamlFile
"""
封装read_excel方法
"""
class Read_Excel:

    def __init__(self,fileName):
        self.fileName=fileName
        global  workbook
        workbook=xlrd.open_workbook(fileName)

    #获取工作簿名称
    def get_SheetName(self):
        sheet=workbook._sheet_names
        return sheet

    def read_Excel(self,name,row,col):
        sheet=workbook.sheet_by_name(name)
        return sheet.row(row)[col].value
    #获取列长度
    def get_RowNums(self, name):
        sheet=workbook.sheet_by_name(name)
        num=sheet.nrows
        return num
    #获取所有case 废弃
    def get_case(self,name):
        cases=[]
        sheet=workbook.sheet_by_name(name)
        print(sheet.nrows)
        for i in range(1,sheet.nrows):
            row_data =sheet.row_values(i)
            print(row_data)
            cases.append(row_data)
        print(cases)
        return cases
if __name__=='__main__':
    YmlList=GetYamlFile.getYamlFile()
    TestCasePath=YmlList["TestCasePath"]
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    REPORT_XLSX_DIR = os.path.join(PROJECT_ROOT, TestCasePath)
    readBook=Read_Excel(REPORT_XLSX_DIR)
    print(readBook.get_case("Request"))
    for sheetName in readBook.get_SheetName():
        print(sheetName)