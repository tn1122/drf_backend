# -*- coding: utf-8 -*-
'''
@Time    : 23-2-8 下午2:58
@Author  : wang
@File    : urls.py
'''
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *
app_name = 'ss_user'


router = DefaultRouter()
router.register('ss_user', SsuserViewSet,basename='ss_user')

urlpatterns = [
] + router.urls