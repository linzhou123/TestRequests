import requests
"""
封装http请求  暂时：post get请求
"""
class HttpBase:
    def __init__(self,url,data,method,headers):
        self.url=url
        self.data=data
        self.method=method
        self.headers=headers
    def getHttpBody(self):
        method={
            "get":requests.get(self.url,params=self.data,headers=self.headers),
            "post":requests.post(self.url,params=self.data,headers=self.headers),
            "Gost":requests.get(self.url,params=self.data,headers=self.headers),
            "Post":requests.post(self.url,params=self.data,headers=self.headers),
         }.get(self.method,requests.get(self.url,params=self.data,headers=self.headers))
        result=method.content
        return result
    def RequestRun(self):
        method={
            "get":requests.get(self.url,params=self.data,headers=self.headers),
            "post":requests.post(self.url,params=self.data,headers=self.headers),
            "Gost":requests.get(self.url,params=self.data,headers=self.headers),
            "Post":requests.post(self.url,params=self.data,headers=self.headers),
         }.get(self.method,requests.get(self.url,params=self.data,headers=self.headers))
        # print(method.content)
        return method


    def getHttpHeaders(self):
        method={
             "get":requests.get(self.url,params=self.data,headers=self.headers),
             "Get":requests.get(self.url,params=self.data,headers=self.headers),
             "post":requests.post(self.url,params=self.data,headers=self.headers),
             "Post":requests.post(self.url,params=self.data,headers=self.headers),
         }.get(self.method,requests.get(self.url,params=self.data,headers=self.headers))
        result=method.headers
        return result











