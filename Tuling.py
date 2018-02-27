# -*- coding: utf-8 -*-

import requests

apiKey = 'e87bd922d08e45eb8b385673f901e06c'
apiUrl = 'http://www.tuling123.com/openapi/api'


def get_response(msg):
    data = {
        'key': apiKey,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        res = requests.post(apiUrl, data=data).json()
        title = res.get('text')
        try:
            return title + "\n\n" + res.get('url')
        except Exception:
            return title
    except Exception:
        return "本宝宝无法理解【" + msg + "】的含义"
