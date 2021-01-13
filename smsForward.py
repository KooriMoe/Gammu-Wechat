#!/usr/bin/env python
import os
import sys
import requests
import json
import datetime
import subprocess

#微信推送程序
pushToWechatPyFile = '/home/ubuntu/Gammu-Wechat/pushToWechat.py'

if __name__ == "__main__":
    #----------------------获取短信内容----------------------
    numParts = int(os.environ['DECODED_PARTS'])
    text = ''
    #单条短信内容
    if numParts == 0:
        text = os.environ['SMS_1_TEXT']
        
    #多条短信内容
    else:
        text = os.environ['DECODED_0_TEXT']

    #发件人
    sender = os.environ['SMS_1_NUMBER']
    #发件日期和时间取当前系统时间
    sendTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #最终发送内容
    sendContent = '发信人: ' + sender + '\n时间: ' + sendTime + '\n\n' + text
    
    #--------------------转发到企业微信程序--------------------
    subprocess.call(['/usr/bin/python3',pushToWechatPyFile,sendContent])