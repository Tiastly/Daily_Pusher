# translate module

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalimt.request.v20181012 import TranslateGeneralRequest

import json
import os

acc_id = os.getenv('Aliyun_acc_id')
acc_key = os.getenv('Aliyun_acc_key')

def translate_zh(text:str):
    
    client = AcsClient(
        f"{acc_id}",  # 阿里云账号的Access Key ID
        f"{acc_key}",# 阿里云账号Access Key Secret
        # "cn-hangzhou"  # 地域ID
        "eu-west-1"
    )
    
    try:
        request = TranslateGeneralRequest.TranslateGeneralRequest()
        request.set_SourceLanguage("de")
        request.set_SourceText(text)
        request.set_FormatType("text")
        request.set_TargetLanguage("zh")

        response = json.loads(client.do_action_with_exception(request))
        # print(response)
        ans = response['Data']['Translated']
        code = response['Code']# detail see https://help.aliyun.com/document_detail/158244.html?spm=a2c4g.11186623.0.0.6c1a5c2aHeFwnV
        print(f"{ans},code = {code}")

    except Exception as e:
        print(e)
        ans = "cannot translate 😢"
        
    return ans

if __name__ == "__main__":
    print(translate_zh("Kartoffel-Gemüse-Omelett"))

