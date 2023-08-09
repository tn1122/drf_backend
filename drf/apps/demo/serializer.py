
### 序列化器的应用与关系
from datetime import datetime
from .models import SsUser
from rest_framework import serializers

# class SsuerSerializer(serializers.Serializer):
#     # 自己定义create, update 等方法 *8
#     # serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义, serializer是独立于数据库之外的存在。
#     # 不需要指定model 模型类
#
#
#     class Meta:
#         SEX_CHOICES = (
#             (1, '男'),
#             (2, '女'),
#             (0, '未知'),
#
#         )
#
#         DELETE_CHOICES = (
#             (1, '删除'),
#             (0, '正常'),
#         )
#
#         ENABLE_CHOICES = (
#             (1, '停用'),
#             (0, '启用'),
#         )
#         user_name = serializers.CharField(max_length=255,)
#         password = serializers.CharField(max_length=255,)
#         sex = serializers.ChoiceField(choices=SEX_CHOICES, default=1, )
#         avatar_url = serializers.CharField(max_length=255, allow_blank=True,)
#         phone = serializers.CharField(max_length=255, allow_blank=True,)
#         create_time = serializers.DateTimeField(default=datetime.now)
#         last_login_time = serializers.DateTimeField(default=datetime.now)
#         email = serializers.CharField(max_length=255, allow_blank=True, label='邮箱')
#         is_delete = serializers.ChoiceField(choices=DELETE_CHOICES, default=0, )
#         is_enable = serializers.ChoiceField(choices=ENABLE_CHOICES, default=0,)
#         remark = serializers.CharField(max_length=255, allow_blank=True, label='备注')
#         user_id = serializers.IntegerField(label='创建用户')
#         is_login = serializers.IntegerField(default=0, label='0 未登录， 1 已登录')
#         user_no = serializers.CharField(allow_blank=True, max_length=255, label='账号')
#         is_admin = serializers.IntegerField(default="0")
#
#     #
#     def create(self, validated_data):
#         return SsUser.objects.create(**validated_data)


class SsuerSerializer(serializers.ModelSerializer):
    # 基于模型类自动生成一系列字段
    # 包含默认的create()和update()的实现
    # 需要制定model 模型类

    class Meta:
        model = SsUser
        fields = '__all__'