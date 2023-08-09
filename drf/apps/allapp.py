# -*- coding: utf-8 -*-
'''
@Time    : 23-2-8 下午3:00
@Author  : wang
@File    : all.py
'''
import re
from importlib import import_module
from django.conf import settings
import logging


URLS_APPS = {}  # 用于自动路由ws/urls、前端左边栏，使django “app”与“project”解耦合
# 相当全局变量

for app in settings.INSTALLED_APPS:
    # 按settings配置app的先后顺序，生成app:urls字典

    try:
        app_model = import_module(f'apps.{app}')  # 尝试import apps.xxx模块
    except Exception:
        continue
    res = re.match(r'(?P<app_name>\w+)($|\.apps\.(?P<app_name2>\w+)Config)', app)
    if res:

        app_name = res.groupdict()['app_name']
        try:
            app_urls = import_module(f'{app_name}.urls')
        except Exception as e:
            print(e)
            if getattr(e, 'name', None) != f'{app}.urls':
                pass
            continue
        URLS_APPS[app_name] = app_urls
