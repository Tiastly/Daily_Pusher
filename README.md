# Description
- 基于微信消息实时推送服务[WxPusher](https://github.com/wxpusher/wxpusher-client)的每天订阅推送服务
- 从bot形式改成了现在的用pub-sub-mode的形式([前情提要](https://github.com/DynAis/wechat-bot/tree/master))
- 代码已经传到阿里云上面每天定时触发
- user只需要在wxPusher中订阅这个应用后就可以每天定时收到推送(每天早八提醒你吃什么中饭)
- 关于虽然每天只用click就能解决的问题,但是还是做了毫无技术力的调包侠🦸‍♂️的这件事XD

API integration, a pusher, and daily routine. The subscriber can receive the daily menu(including translation and pictures) from the university's canteen and the local weather today from dwd(Deutsche Wetter Dienst). Since everything only consists of modules, so it can easily break up.

Das ist ein kleines Programme mit nur die Abfrage der API. Die Ziel liegt im Tagesmenü von der Mensa sowie den Wetterbericht zu wissen.

**好好吃饭** 大切なものです🌟

# To do
## Functions
- [x] 通过request主动获取uid
- [x] 没有menu时候(周末/节假日)显示和平时不一样
- [x] 推送的文本格式拆开变成一个个模块

## API & Source
- [x] Mensa API -> stw-on.de
- [x] 天气模块 -> dwd & bright sky
- [x] 翻译模块 -> Aliyun  
  alternative:Azure Translator
- [x] 食物图片模块 -> serpapi 
  alternative: Google的API 
- [ ] xx模块

*要是出问题了后期换一个*

