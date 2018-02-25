# -*- coding: utf-8 -*-

import json
from urllib import parse, request

isOpen = False


def query_music_info(name):
    try:
        baseurl = 'http://112.74.179.95/search?keywords=' + name
        baseurl = str(baseurl.encode("utf-8")).replace(r"\x", "%")
        req = request.Request(url=baseurl[2:-1])
        res = str(request.urlopen(req).read(), encoding="utf-8")
        # music_url = 'http://112.74.179.95/music/url?id=' + str(json.loads(res)['result']['songs'][0]['id'])
        # music_req = request.Request(url=music_url)
        # music_res = str(request.urlopen(music_req).read(), encoding="utf-8")
        # return json.loads(music_res)['data'][0]['url']
        return "搜索到【" + name + "】,请快点击试听吧：http://music.163.com/song/" + str(
            json.loads(res)['result']['songs'][0]['id']) + "/?userid=38631937"
    except Exception:
        return "哎呀呀，发生了未知错误或者音乐不存在"
