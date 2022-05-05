# 基本功能模块, 提供最基础的机器人逻辑.

from CuteCat import *

def at_me(msg)->bool:
    r"""检测是否@我.

    :param msg: 消息字典
    :return: 是否触发
    """
    if 'wxid=wxid_8xyxdxd49tbp22' in msg['msg'] and '@at' in msg['msg']:
        return True
    else:
        return False

def trigger(msg, trigger_word:str)->bool:
    r"""关键词检测函数.

    :param msg: 消息字典
    :param trigger_word: 关键词
    :return: 是否触发
    """
    if trigger_word in msg['msg']:
        return True
    else:
        return False

def get_raw_text(msg: dict) -> str:
    text = msg["msg"]
    # 删除@
    text = text.replace("[@at,nickname=食堂大妈,wxid=wxid_8xyxdxd49tbp22]", "")
    # 删除前后空格
    text = text.strip()
    return text

def ping(bot: CuteCat, msg: dict)->None:
    print(msg)
    r"""测试函数.

    :param msg: 消息字典
    :return: None
    """
    bot.SendTextMsg(to_wxid= msg.from_wxid, msg = "什么事小伙子")

def help(bot: CuteCat, msg: dict)->None:
    print(msg)
    r"""帮助函数.

    :param msg: 消息字典
    :return: None
    """
    # 发送所有触发关键词
    bot.SendTextMsg(to_wxid= msg.from_wxid, msg = "关键词列表\n1. 菜单\n2. 翻译\n3.js")
    bot.SendTextMsg(to_wxid= msg.from_wxid, msg = "多跟大妈说说话小伙子")
