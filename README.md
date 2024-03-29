# Gammu-Wechat
可以帮助你完成 Gammu + Raspberry Pi 接收短信并推送到企业微信的程序整合包。   
请注意: 如果希望实现企业微信发送短信的功能，**必须**将程序端口(25182)暴露在公网以供调用。你可以通过在路由器设置 NAT 转发并设置 DDNS 解析或利用 Frp 工具实现。

## 配置
在使用前，请先根据企业微信的配置信息编辑 `config.py`.   
```
TOKEN: API接收消息处自定义
EncodingAESKey: API接收消息处自定义
CorpId: 组织ID
Secret: 机器人Secret
agentID: 机器人AgentId
```

## 发送短信
使用前，请确保树莓派的 ```25182``` (或自定义端口) 能够通过公网访问。   
```python3 main.py```   
Usage: !send [发送短信内容] [手机号码]   
Modified from [getway/qyweixin](https://github.com/getway/qyweixin)   

### 保持程序运行
当程序运行的 Session 被关闭后，可能将无法正常收到来自企业微信的发送请求。但是，我们可以利用```Screen```来解决这个问题。   
```
sudo apt-get install screen -y
screen -S "sendSMS"
python3 main.py
```

## 接收短信
关于接收短信的代码来源于 [https://post.smzdm.com/p/a4wme8zx/](https://post.smzdm.com/p/a4wme8zx/)，部署可参照来源文章进行。   

## 短信处理功能(smsProcess.py)
现在，Gammu-Wechat 将在发送微信通知前自动对以下短信内容进行相应处理。   

* 短信验证码: 将验证码提前, 并整合到正文发送来源中。   
* 菜鸟驿站取件码短信: 将取件码提前, 并整合到正文发送来源中。   

如果您希望添加更多功能，您可以向本 Repo 提交 Pull Request.   

* 该功能代码的 LICENSE 为 AGPLv3.

Copyright © 2022 KooriMoe. All rights reserved.
