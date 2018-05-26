# -*- coding: utf-8 -*-

import requests

apiKey = 'e87bd922d08e45eb8b385673f901e06c'
apiUrl = 'http://www.tuling123.com/openapi/api'

xiaodouKey = 'NENXd3UrekE3TD1HbmpDTUNnPVVISDNCcVJZQUFBPT0'
xiaodouUrl = 'http://api.douqq.com/?key=' + xiaodouKey + '&msg='

GONGNENG = '''
############################################################
# .网易搜歌(打开音乐、关闭音乐)
# .报时
# .每日一句
# .抽签
# .猜谜
# .笑话
# .糗事
# .QQ号(94113786)
# .md5+空格+欲加密的内容(md5加密admin)
# .计算13-2
# .城市名+空气质量(厦门空气质量)
# .城市名+天气(厦门天气)
# .身份证号(330282197908022538)
# .ip地址(112.64.235.86)
# .手机号(13838383838)
# .拼音+欲转的汉字(拼音我)
# .快递+单号(快递1106279322505)
# .藏头诗+开头的字(藏头诗我为秋香)
# .翻译+中文(翻译我爱你)
# .一言(一言)
# .银行卡+卡号(银行卡6228481552887309119)
# .人民币数字转大写 大写+数字(大写1542)
# .人品+姓名(人品刘小虎)
# .磁力+电影名称(磁力变形金刚)
# .梦见+梦中的事物(梦见结婚)
# .字典+汉字(字典豆)
# .词典+汉字(词典小豆)
# .成语+汉字(成语大智若愚)
# .点歌+歌名(点歌小苹果)
# .歌词+歌名(歌词小苹果)
# .疾病名+症状(感冒症状)
# .疾病名+病因(感冒病因)
# .疾病名+怎么治疗(感冒怎么治疗)
# .菜名+的做法(豆沙包的做法)
# .什么是+名词(什么是机器人)
# .历史上的今天
# .百家姓(李)
# .xxx的原因 或 为什么***(引起头晕的原因 或者 为什么我的电脑很卡)
# .电影+影片名(电影疯狂动物城)
# .短网址+网页地址(短网址http://www.baidu.com)
# .脑筋急转弯(脑筋急转弯)
# .你与我的距离(距离、你在哪)
# .成语接龙
############################################################
'''


def get_response(msg):
    try:
        res = requests.get(xiaodouUrl + msg)
        try:
            if res.text.__contains__("<html>"):
                return get_tuling(msg)
            else:
                return res.text.replace("小豆", "本宝宝")
        except Exception:
            return get_tuling(msg)
    except Exception:
        return "本宝宝无法理解【%s】的含义" % msg


def get_tuling(msg):
    data = {
        'key': apiKey,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        res = requests.post(apiUrl, data=data).json()
        title = res.get('text')
        try:
            return title
        except Exception:
            return "本宝宝无法理解【%s】的含义" % msg
    except Exception:
        return "本宝宝无法理解【%s】的含义" % msg
