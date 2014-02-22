import web
import hashlib
import os
import time
from lxml import etree


class Entrance:
    '''
      Weixin Official Account Entrance
    '''
    def __init__(self):
        self.token = 'banshan'
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        '''
          Deal with GET request
        '''
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr

        return self.validation(signature, timestamp, nonce, echostr)

    def validation(self, signature, timestamp, nonce, echostr):
        '''
          Check if request from Weixin
        '''
        params = {
            'token': self.token,
            'timestamp': timestamp,
            'nonce': nonce
        }

        if self.is_not_none(params):
            sort_params = sorted([v for k, v in params.items()])
            client_signature = hashlib.sha1(''.join(sort_params)).hexdigest()

            if client_signature == signature:
                return echostr
        return False

    def is_not_none(self, params):
        '''
          Check all values in map not none.
        '''
        for k, v in params.items():
            if v is None:
                return False
        return True

    def POST(self):
        str_xml = web.data()  # 获得post来的数据
        xml = etree.fromstring(str_xml)  # 进行XML解析
        content = xml.find("Content").text  # 获得用户所输入的内容
        # msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        return self.render.reply_text(fromUser,toUser, int(time.time()), u"我现在还在开发中，还没有什么功能，您刚才说的是：" + content)
