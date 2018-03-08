# -*- coding: utf-8 -*-

import json
import requests
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
HELP_MSG = u'''\
欢迎使用微信网易云音乐
音乐： 开始音乐
关闭： 关闭歌曲
歌名： 按照引导播放音乐\
'''

isOpen = False


def query_music_info(name):
    resStr = ""
    sum = 0
    try:
        req = requests.get('http://112.74.179.95/search?keywords=' + name)
        req.encoding = "utf-8"
        print req.text
        data = json.loads(req.text)['result']
        print data
        for index in range(int(data['songCount'])):
            sum += 1
            music_name = "%s  %s" % (data['songs'][index]['artists'][0]['name'], data['songs'][index]['name'])
            resStr += "\n\n[%s] ,请快点击试听吧：http://music.163.com/song/%s/?userid=38631937" % (
                music_name, data['songs'][index]['id'])
        return "为您搜到%s首音乐%s" % (str(sum), resStr)
    except IndexError:
        return "为您搜到%s首音乐%s" % (str(sum), resStr)
    except Exception:
        return "哎呀呀，发生了未知错误或者音乐不存在"
