# -*- coding: utf-8 -*-

import itchat

from itchat.content import *
import wechat_robot.Chat as Chat

itchat.auto_login()


@itchat.msg_register(TEXT)
def text_reply(msg):
    return Chat.has_music(msg['Text'])


chatroom_ids = ['牛逼不吹，我会死呀']


@itchat.msg_register([TEXT, SHARING, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def group_reply_text(msg):
    print("msg = %s" % msg)
    chatroom_id = msg['User']['NickName']
    username = msg.actualNickName
    if not chatroom_id in chatroom_ids:
        return
    if msg['Type'] == TEXT:
        msg.user.send('@%sX %s' % (username, text_reply(msg)))
    if msg['Type'] in [MAP, CARD, NOTE, SHARING]:
        msg.user.send('@%s\u2005 %s %s' % (username, msg.type, msg.text))
    if msg['Type'] in [PICTURE, RECORDING, ATTACHMENT, VIDEO]:
        msg.download(msg.fileName)
        typeSymbol = {
            PICTURE: 'img',
            VIDEO: 'vid', }.get(msg.type, 'fil')
        msg.user.send('@%s\u2005' % username)
        return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register([MAP, CARD, NOTE, SHARING])
def map_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('您好！')

itchat.run()
