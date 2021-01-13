#!/usr/bin/env python

# Gammu-Wechat - pushToWechat.py
# The original author: https://post.smzdm.com/p/a4wme8zx/
# Edited by TheZihanGu.

import os
import sys
import requests
import json
import config

#企业微信发送消息
def entWechatSend(corpID,secret,agentID,content):
    #获取token
    tokenUrl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    result = requests.get(tokenUrl,params={'corpid':corpID,'corpsecret':secret})
    accessToken = None

    if result.status_code != 200:
        print('连接到服务器失败')
    else:
        resultJson = json.loads(result.text)

        if resultJson['errcode'] != 0:
            print('响应结果不正确')
        else:
            accessToken = resultJson['access_token']
            #print(accessToken)
                
    #发送消息
    reqUrl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}" 
    """
    touser  成员 @all 就是所有
    toparty 部门ID @all 就是所有
    msgtype 文本类型
    agentid 企业应用ID
    content 内容
    safe 是否保密 0是不保密
    """
    values = {
            "touser"  : "@all",
            "toparty" : "@all",
            "msgtype" : "text",
            "agentid" : agentID,
            "text"    : {
                "content" : content
                },
            "safe"    :"0"
            }
    
    sendData = json.dumps(values)
    result = requests.post(reqUrl.format(accessToken),sendData)
    #print(result.text)

if __name__ == "__main__":
    '''
    执行脚本范例：
    python pushToWechat.py content
    '''
    #--------------------获取企业微信配置信息--------------------
    #企业ID
    corpID = config.CorpId
    #应用密钥
    secret  = config.Secret
    #应用ID
    agentID = config.agentID
    

    #-----------------------获取发送内容-----------------------
    content = sys.argv[1]
    
    #----------------------推送到企业微信----------------------
    entWechatSend(corpID,secret,agentID,content)