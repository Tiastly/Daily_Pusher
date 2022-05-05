# 大妈作为翻译机器人

import deepl
from CuteCat import *
from Essential import *



auth_key="061ff7db-0d41-e41f-43d5-023e19183457:fx"
translator = deepl.Translator(auth_key)


def translate_to_zh(bot: CuteCat, msg: dict) -> str:
    text = text.replace("翻译", "")
    text = get_raw_text(msg)
    print("翻译:"+text)
    result = translator.translate_text(text, target_lang="ZH")
    bot.SendTextMsg(to_wxid= msg.from_wxid, msg = result.text)
    print("翻译结果: "+result.text)

def translate_raw_text_zh(text: str) -> str:
    result = translator.translate_text(text, target_lang="ZH")
    return result.text
