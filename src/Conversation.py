# 大妈作为聊天机器人

import os
import openai
from CuteCat import *
from Essential import *

openai.api_key = "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"



def ask(bot: CuteCat, msg: dict) -> str:
    start_sequence = "\n食堂大妈:"
    restart_sequence = "\n学生: "
    text = get_raw_text(msg)
    print(text)
    prompt_text = "以下是一个学生与食堂大妈的对话.食堂大妈善于聊天, 但是性格有些不耐烦, 会称呼学生为小伙子, 大妈今年已经56岁了.\n\n\
                  学生: 一公斤有多少磅.\n\
                  食堂大妈: 小伙子怎么连这个都不知道, 一公斤有2.2磅.\n\
                  学生: HTML是什么\n\
                  食堂大妈: 小伙子这种东西么自己查一下嘛？ 超文本标记语言. 以后问点有营养的问题好不好啦？\n\
                  学生: 生命的意义是什么？\n\
                  食堂大妈: 不知道, 不如想想晚上吃什么, 小伙子\n\
                  学生: "
    # GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text + text + start_sequence,
        temperature=0.8,
        max_tokens=150,
        top_p=0.8,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    print(response)
    bot.SendTextMsg(to_wxid= msg.from_wxid, msg = response["choices"][0]["text"])

def js_helper(bot: CuteCat, msg: dict) -> str:
    start_sequence = "\nJavaScript聊天机器人:"
    restart_sequence = "\n你: "
    text = get_raw_text(msg)
    print(text)
    prompt_text = "你: 如何组合数组\n\
                  JavaScript聊天机器人: 你可以使用concat()方法.\n\
                  你: 如何让一个警报在10秒后出现\n\
                  JavaScript聊天机器人: 你可以使用setTimeout()方法使警报在10秒后出现.\n\
                  你: "
    response = openai.Completion.create(
      engine="code-davinci-002",
      prompt= prompt_text + text + start_sequence,
      temperature=0,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.5,
      presence_penalty=0,
      stop=["你:"]
    )
    print(response)
    bot.SendTextMsg(to_wxid= msg.from_wxid, msg = response["choices"][0]["text"])