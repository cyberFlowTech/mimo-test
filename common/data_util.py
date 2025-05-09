import os

import yaml

def readYaml(path):
    with open(path,'r+',encoding="utf-8") as file:
        #绝对路径
        data = yaml.load(stream=file,Loader=yaml.FullLoader)
        #相对路径
        # data = yaml.safe_load(file)
        return data

