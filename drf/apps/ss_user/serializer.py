# -*- coding: utf-8 -*-
'''
@Time    : 23-2-8 下午4:19
@Author  : wang
@File    : serializer.py
'''
from rest_framework import serializers
from .models import SsUser

class SsUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SsUser

        fields = '__all__'


    # 验证
