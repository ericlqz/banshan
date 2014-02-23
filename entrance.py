# -*- coding: utf-8 -*-
#created:      Thu Feb  8 18:27:11 2014
#filename:     entrance.py
#author:       eric lin
#email:        linqingzu@gmail.com

import web
import os
import sys

# 在import自己的包之前要先把路径加到系统的path
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
