#!/usr/bin/env python
import os
import sys
import requests
import json
import datetime
import subprocess
import re

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
        for i in range(1, numParts + 1):
            varname = "DECODED_%d_TEXT" % i
            if varname in os.environ:
                text = text + os.environ[varname]

    #发件人
    sender = os.environ['SMS_1_NUMBER']
    #发件日期和时间取当前系统时间
    sendTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # BEGIN SMSPROCESS.PY
    # 短信来源识别
    def getSource(content):
        rule = r"【(.*?)】"
        smsSource = ','.join(re.findall(rule, content))
        return smsSource

    # 菜鸟驿站提醒短信识别
    if "【菜鸟驿站】" and "取件" in text:
        pickupCode = ','.join(re.findall("\d{2}-\d{1}-\d{4}", text))
        finalContent = "[菜鸟驿站:%s] "%pickupCode + text.replace("【菜鸟驿站】", "")
        text = finalContent

    # 验证码短信识别
    if "验证码" in text:
        captchaCode = ','.join(re.findall("\d{6}|\d{4}", text))
        smsSource = getSource(text)
        finalContent = "[%s:"%smsSource + "%s] "%captchaCode + text.replace("【%s】"%smsSource, "")
        text = finalContent
    # END SMSPROCESS.PY

    #最终发送内容
    sendContent = '发信人: ' + sender + '\n时间: ' + sendTime + '\n\n' + text
    
    #--------------------转发到企业微信程序--------------------
    subprocess.call(['/usr/bin/python3',pushToWechatPyFile,sendContent])
