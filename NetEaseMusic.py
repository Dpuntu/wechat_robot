# -*- coding: utf-8 -*-

import json
from urllib import request

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
        baseUrl = 'http://112.74.179.95/search?keywords=' + name
        baseUrl = str(baseUrl.encode("utf-8")).replace(r"\x", "%")
        req = request.Request(url=baseUrl[2:-1])
        res = str(request.urlopen(req).read(), encoding="utf-8")
        data = json.loads(res)['result']
        print(data)
        for index in range(int(data['songCount'])):
            sum += 1
            music_id = data['songs'][index]['id']
            music_name = data['songs'][index]['artists'][0]['name'] + "——" + data['songs'][index]['name']
            resStr += "\n\n搜索到【" + music_name + "】,请快点击试听吧：http://music.163.com/song/" + str(
                music_id) + "/?userid=38631937"
        return "为您搜到" + str(sum) + "首音乐" + resStr
    except IndexError:
        return "为您搜到" + str(sum) + "首音乐" + resStr
    except Exception:
        return "哎呀呀，发生了未知错误或者音乐不存在"
