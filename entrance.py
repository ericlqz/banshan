# -*- coding: utf-8 -*-
import web
import os
import sys

# 在import自己的包之前要先把路径加到系统的path中
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)

from weixinInterface import Entrance

urls = (
    '/', 'Entrance',
)

application = web.application(urls, globals()).wsgifunc()
web.webapi.internalerror = web.debugerror

if __name__ == '__main__':
    application.run()
