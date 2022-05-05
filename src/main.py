""" 接收事件类型
    on_group_msg = on('EventGroupMsg')
    on_friend_msg = on('EventFriendMsg')
    on_received_transfer = on('EventReceivedTransfer')
    on_friend_vertify = on('EventFriendVerify')
    on_sendout_msg = on('EventSendOutMsg')
    on_sys_msg = on('EventSysMsg')
    on_login = on('EventLogin')
"""
""" 发送事件类型
    def SendTextMsg(self, to_wxid : str, msg : str):...
    def SendImageMsg(self, to_wxid : str, msg : str):...
    def SendVideoMsg(self, to_wxid : str, msg : str):...
    def SendFileMsg(self, to_wxid : str, msg : str):...
    def GetRobotName(self) -> str:...
    def GetFriendList(self) -> List[Dict[str, Any]]:...
    def GetGroupList(self) -> List[Dict[str, Any]]:...
    def GetGroupMemberList(self, group_wxid : str) -> List[Dict[str, Any]]:...
    def GetGroupMemberInfo(self, group_wxid : str, member_wxid : str) -> Dict[str, Any]:...
    def AcceptTransfer(self, to_wxid : str, msg : str):...
    def AgreeGroupInvite(self, msg : str):...
    def AgreeeFriendVerify(self, msg : str):...
    def GetAppDir(self) -> str:...
"""

from CuteCat import *
from Essential import *
from Mensa import *
from Conversation import *
from Translate import *



# 生成机器人实例
bot = CuteCat( api_url = 'http://127.0.0.1:8090' , robot_wxid = 'wxid_8xyxdxd49tbp22')



@bot.on('EventFriendMsg')
def on_admin_msg(msg):
  # 大妈的有限状态机, 一次对话只能最多触发一个函数

  # 优先度 1
  if trigger(msg, "菜单"): pull_mensa_menu(bot, msg) # 拉取食堂菜单, 关键词{菜单}
  elif trigger(msg, "/help"): help(bot, msg) # 帮助, 关键词{@+/help}
  elif trigger(msg, "翻译"): translate_to_zh(bot, msg) # 翻译, 关键词{翻译}
  # 优先度 10
  else: ask(bot, msg) # 对话, 无关键词



@bot.on('EventGroupMsg')
#匹配群信息
def on_general_group_msg(msg):
  # 大妈的有限状态机, 一次对话只能最多触发一个函数

  # 优先度 0
  # if at_me(msg): ping(bot, msg) # 测试, 关键词{@}
  if at_me(msg) and trigger(msg, "/help"): help(bot, msg) # 帮助, 关键词{@+/help}
  # 优先度 1
  elif at_me(msg) and trigger(msg, "菜单"): pull_mensa_menu(bot, msg) # 拉取食堂菜单, 关键词{@+菜单}
  elif at_me(msg) and trigger(msg, "翻译"): translate_to_zh(bot, msg) # 翻译, 关键词{翻译}
  elif at_me(msg) and trigger(msg, "js"): js_helper(bot, msg) # js辅助, 关键词{@+js}
  # 优先度 10
  elif at_me(msg): ask(bot, msg) # 对话, 无关键词
  # elif trigger(msg, "大妈"): ask(bot, msg)



# 开始监听
# bot.SendTextMsg(to_wxid= '20496408956@chatroom', msg = '上班')
bot.run()

# TODO: 1.关键词字典触发