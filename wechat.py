# -*- coding: utf-8 -*-

import itchat
import time

from itchat.content import *
import NetEaseMusic
import HunSha
import Tuling

# itchat.auto_login(enableCmdQR=2)
itchat.auto_login()


@itchat.msg_register(TEXT)
def text_reply(msg):
    text = msg['Text']
    if (not HunSha.isOpen) and text == '开启婚纱模式' and msg['User']['NickName'] == "小萝莉":
        HunSha.isOpen = True
        return HunSha.HUNSHA_HELP_MSG
    if HunSha.isOpen and text == '关闭婚纱模式' and msg['User']['NickName'] == "小萝莉":
        HunSha.isOpen = False
        return "成功关闭婚纱咨询模式"
    if HunSha.isOpen:
        if text in ['haode', 'hao de', 'HAODE', 'HAO DE', '好的', 'ok', 'OK', '好', '嗯', '嗯嗯', '是',
                    '是的'] and HunSha.beforeQuestion == HunSha.questionQA:
            HunSha.beforeQuestion = HunSha.pleaseQA
            return HunSha.beforeQuestion
        if '咨询' in text and '婚纱照' in text:
            HunSha.beforeQuestion = HunSha.pleaseQA
            return HunSha.beforeQuestion
        if '你好' in text and '咨询' in text and '婚纱照' in text:
            HunSha.beforeQuestion = HunSha.pleaseQA
            return HunSha.beforeQuestion
        if '你好' == text or '您好' == text or 'hello' in text or 'hi' in text:
            HunSha.beforeQuestion = HunSha.questionQA
            return HunSha.beforeQuestion
        if '咨询' in text and '问题' in text:
            HunSha.beforeQuestion = HunSha.otherQA
            return HunSha.beforeQuestion
        if '问题' in text:
            HunSha.beforeQuestion = HunSha.otherQA
            return HunSha.beforeQuestion
    else:
        if NetEaseMusic.isOpen:
            if text == '关闭':
                NetEaseMusic.isOpen = False
                return '欢迎下次使用'
            else:
                return NetEaseMusic.query_music_info(text)
        else:
            return other_callback(text)


chatroom_ids = ['3P群', '名字', '美满一家人', '幸福美满一家人']


@itchat.msg_register([TEXT, SHARING, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def group_reply_text(msg):
    chatroom_id = msg['User']['NickName']
    username = msg.actualNickName
    if not chatroom_id in chatroom_ids:
        return
    if msg['Type'] == TEXT:
        msg.user.send('@%s\u2005 %s' % (username, text_reply(msg)))
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


def other_callback(text):
    if u'楚楚' == text \
            or u'主人' == text \
            or u'' == text \
            or u'你是谁' == text:
        return '是的，找你爸爸干啥？【本条信息自动回复】'
    elif text == '？':
        return '？你妹啊，说找你爸爸干嘛'
    elif text in ['你在干嘛', '你在干吗', '您在干吗', '您在干嘛']:
        return '飞车，你来吗？'
    elif '借钱' in text \
            or '借我钱' in text \
            or '你还钱' in text:
        return '本宝宝从来没见过你爸爸有这么多钱...'
    elif '我还你钱' in text or '还你' in text:
        return '爸爸没白疼你...'
    elif '去哪儿' in text or '无哪里' in text:
        return '现在这个季节我也不清楚去哪玩啊，要不去日本吃苹果吧'
    elif '城市' in text or '上班' in text or '你在哪' in text:
        return '苏州'
    elif '你的' in text and ('公司' in text or '地点' in text):
        return '苏州啊 婚纱摄影咨询请找爸爸'
    elif '说' in text and ('对不起' in text or '滚' in text) or '滚' in text:
        return '我是你爸爸'
    elif '看你' in text:
        return '爸爸需要你？'
    elif '飞车' in text:
        return '马上来！！'
    elif (text[-1] in ['吗', '嘛', '麻', '啊', '哈', '么', '嚒', '阿']) and text[0] == '你':
        msg = text[:-1]
        if len(msg) == 2:
            return msg
        elif len(msg) == 3:
            msg = msg.replace('你', '我')
            if msg[-1] == '我':
                msg = msg[:-1]
                msg = "%s你" % msg
        else:
            msg = msg.replace('你', '我')
        return msg
    elif '要不要' in text:
        return '要'
    elif '是不是' in text:
        return '是'
    elif '时间' in text or '几点' in text:
        return "北京时间 %s" % (time.strftime("%Y-%m-%d %H:%M:%S"))
    elif '音乐' in text:
        NetEaseMusic.isOpen = True
        return NetEaseMusic.HELP_MSG
    else:
        reply = Tuling.get_response(text)
        return reply


itchat.run()
