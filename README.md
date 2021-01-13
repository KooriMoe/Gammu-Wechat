# Gammu-Wechat
可以帮助你完成 Gammu + Raspberry Pi 接收短信并推送到企业微信的程序整合包。   
请注意，本项目的部分功能仅支持拥有公网环境下使用。

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

## 接收短信
关于接收短信的代码来源于 [https://post.smzdm.com/p/a4wme8zx/](https://post.smzdm.com/p/a4wme8zx/)，部署可参照来源文章进行。   