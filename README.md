## WechatPush

基于 [企业微信 API](https://developer.work.weixin.qq.com/document/path/90236) 的微信消息推送, 无需自建服务器的 Python 库解决方案.

#### 前言

很多时候编写程序时希望能将程序的运行结果实时告知开发者, 需要点对点的推送服务.

Telegram Bot 国内使用不便, 现有的微信推送大多需要使用第三方服务器, 接口调用有限制.

**而此 Python 库有以下优点:**

- **无需自建服务器, 不使用第三方服务器, 无其他费用**
- **第一次需要配置(只需要个人微信), 之后可以直接调用, 简单方便**
- **无需安装企业微信客户端, 可以直接在微信接收推送**
- **调用次数充足, 限制少**
- **可以推送 文本, 超链接, 图片, 文件, Markdown 多种格式**

#### 配置(本步内容参考了 [WecomChan](https://github.com/easychen/wecomchan) 的相关文档)

**配置过程中, 你需要记录下 `corp_id` `secret` 以及 `agent_id` 三个值.**

- **第一步，注册企业**

  用电脑打开[企业微信官网](https://work.weixin.qq.com/)，注册一个企业

- **第二步，创建应用**

  注册成功后，点「管理企业」进入管理界面，选择「应用管理」 → 「自建」 → 「创建应用」

  [![img](https://camo.githubusercontent.com/c85602d131ba9fc1febf43aa851933ddaf0e7a36a7d334e2c51b497798550eea/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134333232382e706e67)](https://camo.githubusercontent.com/c85602d131ba9fc1febf43aa851933ddaf0e7a36a7d334e2c51b497798550eea/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134333232382e706e67)

  应用名称可以随意填入，应用logo自己上传一张图片，可见范围选择公司名。

  [![img](https://camo.githubusercontent.com/f590bd0f72c741936fcf081ed5ad6ad6e62fe64b003b090693457a46078c4a2a/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134333332372e706e67)](https://camo.githubusercontent.com/f590bd0f72c741936fcf081ed5ad6ad6e62fe64b003b090693457a46078c4a2a/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134333332372e706e67)

  创建完成后进入应用详情页，可以得到  `agent_id`，应用Secret( `secret` )。

  注意：`secret`推送到手机端时，只能在`企业微信客户端`中查看。

  [![img](https://camo.githubusercontent.com/ec3ddd2dd460680f9fc61acc8a1bd215fcb947608102764539c4ce43bc1e0f26/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134333535332e706e67)](https://camo.githubusercontent.com/ec3ddd2dd460680f9fc61acc8a1bd215fcb947608102764539c4ce43bc1e0f26/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134333535332e706e67)

  **2022年6月20日之后创建的应用，需要额外配置可信IP。**

  在「应用详情页」的最下方，开发者接口分类中，找到「企业可信IP」，点击「配置」，并填入服务器IP即可。

  注意，如果你使用云函数等公用IP的云服务，可能需要在（云函数或其他服务的）设置界面中打开「固定公网IP」来获得一个独立的IP。否则有可能报「第三方服务IP」错误。

- **第三步，获取企业ID**

  进入「[我的企业](https://work.weixin.qq.com/wework_admin/frame#profile)」页面，拉到最下边，可以看到企业ID(`corp_id`)③，复制并填到上方。

  推送UID直接填 `@all` ，推送给公司全员。

- **第四步，推送消息到微信**

  进入「我的企业」 → 「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到下边扫描二维码，关注以后即可收到推送的消息。

  [![img](https://camo.githubusercontent.com/cada0b7dcec30ab707403c0cf22380a25442eddb44a4e173230cfab3e8e9b1b8/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134343830382e706e67)](https://camo.githubusercontent.com/cada0b7dcec30ab707403c0cf22380a25442eddb44a4e173230cfab3e8e9b1b8/68747470733a2f2f746865736576656e2e667471712e636f6d2f32303231303230383134343830382e706e67)

  PS：如果出现`接口请求正常，企业微信接受消息正常，个人微信无法收到消息`的情况：

  进入「我的企业」 → 「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到最下方，勾选 “允许成员在微信插件中接收和回复聊天消息” [![img](https://camo.githubusercontent.com/e7f6132a7b2414f1b768124c994ae18374d078e5c7fe08b14d8e84c0947825de/68747470733a2f2f696d672e616d73312e696d676265642e78797a2f323032312f30362f30312f48504952552e6a7067)](https://camo.githubusercontent.com/e7f6132a7b2414f1b768124c994ae18374d078e5c7fe08b14d8e84c0947825de/68747470733a2f2f696d672e616d73312e696d676265642e78797a2f323032312f30362f30312f48504952552e6a7067)

  在企业微信客户端 「我」 → 「设置」 → 「新消息通知」中关闭 “仅在企业微信中接受消息” 限制条件 [![img](https://camo.githubusercontent.com/5a99484e846f78071bd1376180920ce35070211f20f1dda507880a111b017d0b/68747470733a2f2f696d672e616d73312e696d676265642e78797a2f323032312f30362f30312f48504b50582e6a7067)](https://camo.githubusercontent.com/5a99484e846f78071bd1376180920ce35070211f20f1dda507880a111b017d0b/68747470733a2f2f696d672e616d73312e696d676265642e78797a2f323032312f30362f30312f48504b50582e6a7067)

#### 安装

```shell
pip3 install wechat_push
```

#### 示例

```python
>>> from wechat_push import WechatPush
>>> push = WechatPush("你的corp_id", "你的secret", "你的agent_id")
>>> push.send_text('Hello!\n文本支持换行\n<a href="https://github.com">文本支持超链接</a>')
{'errcode': 0, 'errmsg': 'ok', 'msgid': 'xxx'}
>>> push.send_markdown("**Markdown here!**")
{'errcode': 0, 'errmsg': 'ok', 'msgid': 'xxx'}
>>> push.send_file(open("test.txt", "rb"), "微信中显示的文件名称")
{'errcode': 0, 'errmsg': 'ok', 'msgid': 'xxx'}
>>> push.send_image(open("test.png", "rb"))
{'errcode': 0, 'errmsg': 'ok', 'msgid': 'xxx'}
```

