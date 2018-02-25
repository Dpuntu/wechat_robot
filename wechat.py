# -*- coding: utf-8 -*-

import itchat
import time

from itchat.content import *
import NetEaseMusic

itchat.auto_login(hotReload=True)

HELP_MSG = u'''\
欢迎使用微信网易云音乐
音乐： 显示帮助
关闭： 关闭歌曲
歌名： 按照引导播放音乐\
'''


@itchat.msg_register(TEXT)
def text_reply(msg):
    text = msg['Text']
    if NetEaseMusic.isOpen:
        if text == '关闭':
            NetEaseMusic.isOpen = False
            return '欢迎下次使用'
        else:
            return NetEaseMusic.query_music_info(text)
    else:
        if u'楚楚' == text \
                or u'主人' == text \
                or u'' == text \
                or u'你是谁' == text:
            return '是的，找你爸爸干啥？【本条信息自动回复】'
        elif text == '？':
            return '？你妹啊，说找你爸爸干嘛'
        elif '你在干嘛' == text \
                or '你在干吗' == text \
                or '您在干吗' == text \
                or '您在干嘛' == text:
            return '写代码啊, if（mNum>PI）print("${mNum*3}+PI")'
        elif '到那了' in text or '到哪了' in text:
            return '我无法知道你爸爸的位置哟！你可以电话联系:17521128368'
        elif '借钱' in text \
                or '借我钱' in text \
                or '你还钱' in text:
            return '本宝宝从来没见过你爸爸有这么多钱...'
        elif '我还你钱' in text or '还你' in text:
            return '爸爸没白疼你...'
        elif '去哪儿' in text or '无哪里' in text:
            return '现在这个季节我也不清楚去哪玩啊，要不去日本吃苹果吧'
        elif '城市' in text or '上班' in text or '你在哪' in text:
            return '上海'
        elif '你的' in text and ('公司' in text or '地点' in text):
            return '再惠啊 http://www.kezaihui.com/#!/'
        elif '说' in text and ('对不起' in text or '滚' in text) or '滚' in text:
            return '我是你爸爸'
        elif '看你' in text:
            return '爸爸需要你？'
        elif '电影' in text:
            return '最近没啥看的'
        elif '飞车' in text:
            return '马上来！！'
        elif ('吗' == text[-1]
              or '嘛' == text[-1]
              or '麻' == text[-1]
              or '啊' == text[-1]
              or '哈' == text[-1]
              or '么' == text[-1]
              or '嚒' == text[-1]
              or '阿' == text[-1]) and text[0] == '你':
            msg = text[:-1]
            if len(msg) == 2:
                return msg
            elif len(msg) == 3:
                msg = msg.replace('你', '我')
                if msg[-1] == '我':
                    msg = msg[:-1]
                    msg = msg + "你"
            else:
                msg = msg.replace('你', '我')
            return msg
        elif '要不要' in text:
            return '要'
        elif '是不是' in text:
            return '是'
        elif '时间' in text or '几点' in text:
            return "北京时间" + time.strftime("%Y-%m-%d %H:%M:%S")
        elif '音乐' in text:
            NetEaseMusic.isOpen = True
            return HELP_MSG
        elif len(text) <= 5:
            return text
        else:
            return '本宝宝无法理解"' + text + '"的含义'


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
    msg.user.send('喂，那傻狗！我是你爸爸')


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


itchat.run()
