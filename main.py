#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from __future__ import absolute_import, unicode_literals
from flask import Flask, request, abort, render_template
from wechatpy.enterprise.crypto import WeChatCrypto
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.enterprise.exceptions import InvalidCorpIdException
from wechatpy.enterprise import parse_message, create_reply
from wechatpy.enterprise.replies import ImageReply
import requests
import json
import config
import os
from wechatpy.enterprise.client.api.media import WeChatMedia
from wechatpy.enterprise import WeChatClient

client = WeChatClient(config.CorpId, config.Secret)

TOKEN = config.TOKEN
EncodingAESKey = config.EncodingAESKey
CorpId = config.CorpId

app = Flask(__name__)

@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    signature = request.args.get('msg_signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')

    crypto = WeChatCrypto(TOKEN, EncodingAESKey, CorpId)
    if request.method == 'GET':
        echo_str = request.args.get('echostr', '')
        try:
            echo_str = crypto.check_signature(
                signature,
                timestamp,
                nonce,
                echo_str
            )
        except InvalidSignatureException:
            abort(403)
        return echo_str
    else:
        try:
            msg = crypto.decrypt_message(
                request.data,
                signature,
                timestamp,
                nonce
            )
        except (InvalidSignatureException, InvalidCorpIdException):
            abort(403)
        msg = parse_message(msg)
        user_name = msg.source
        help_message = "Usage: !send [Text] [Phone Number]"
        if msg.type == 'text':
            message = msg.content
            if message == 'help':
                reply = create_reply(help_message, msg).render()
                res = crypto.encrypt_message(reply, nonce, timestamp)
                return res
            if "!send" in message:
                message2 = message.replace("!send ", "")
                text = message2.split(" ")[0]
                phone = message2.replace(text + " ", "")
                status = os.popen("echo " + text + " | sudo gammu sendsms TEXT " + phone).read()
                reply = create_reply("收信人: " + phone + "\n短信内容: " + text + "\n状态: " +  status, msg).render()
                res = crypto.encrypt_message(reply, nonce, timestamp)
                return res
            else:
                message = help_message
                reply = create_reply(message, msg).render()
                res = crypto.encrypt_message(reply, nonce, timestamp)
                return res
        return ''


if __name__ == '__main__':
    app.run('0.0.0.0', 25182, debug=False)