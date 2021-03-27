# Gammu-Wechat
可以帮助你完成 Gammu + Raspberry Pi 接收短信并推送到企业微信的程序整合包。   
请注意，若想完成企业微信操作发送短信的行为，**必须**让程序端口(25182)暴露在公网。这个步骤可有多种解决方法，例如路由器端口映射+DDnS(适用于拥有公网IP的环境)或利用内网穿透/FRP进行。

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