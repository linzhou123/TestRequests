import os
import yaml
"""
获取config.yml文件内容
"""
def getYamlFile():
    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    CONFIG_PATH=os.path.join(PROJECT_ROOT,'Config.yml')
    ConfigData=open(CONFIG_PATH)
    YmlList=yaml.load(ConfigData,Loader=yaml.FullLoader)
    return YmlList