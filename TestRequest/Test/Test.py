import time
import os
print(time.strftime("%Y_%m_%d"))
print(type(time.strftime("%Y_%m_%d")))

dirname=os.path.dirname(os.path.dirname(__file__))
path =os.path.join(dirname,"CaseResult","test","1111")
print(path)