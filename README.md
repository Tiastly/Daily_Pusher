# Description
- 基于微信消息实时推送服务[WxPusher](https://github.com/wxpusher/wxpusher-client)的每天订阅推送服务
- 从bot形式改成了现在的用pub-sub-mode的形式([前情提要](https://github.com/DynAis/wechat-bot/tree/master))
- 代码已经传到阿里云上面每天定时触发
- user只需要在wxPusher中订阅这个应用后就可以每天定时收到推送(每天早八提醒你吃什么中饭)
- 关于虽然每天只用click就能解决的问题,但是还是做了毫无技术力的调包侠🦸‍♂️的这件事XD

# To do
## Functions
- [x] 通过request主动获取uid
- [ ] 没有menu时候(周末/节假日)显示和平时不一样
- [ ] 推送的文本格式拆开变成一个个模块

## API & Source
- [x] Mensa API -> stw-on.de
- [ ] 天气模块 -> dwd
- [x] 翻译模块 -> Aliyun 可选:Azure Translator
- [x] 食物图片模块 -> serpapi 
  后期可能换成Google的API 
- [ ] xx模块
## 优化(?)
- [ ] 运行日志
- [ ] 改成异步模式

# 好好吃饭 
大切なものです🌟

# 库
```pip install -U wxpusher```\
```pip install google-search-results```

```pip install aliyun-python-sdk-core-v3```\
```pip install aliyun-python-sdk-alimt```\
