from django.db import models

# Create your models here.

class SsUser(models.Model):

    SEX_CHOICES = (
        (1, '男'),
        (2, '女'),
        (0, '未知'),

    )

    DELETE_CHOICES = (
        (1, '删除'),
        (0, '正常'),
    )

    ENABLE_CHOICES = (
        (1, '停用'),
        (0, '启用'),
    )

    user_name = models.CharField(max_length=255, null=False, verbose_name='用户名')
    password = models.CharField(max_length=255, null=False, verbose_name='密码')
    sex = models.SmallIntegerField(choices=SEX_CHOICES,default=1, verbose_name='0 未知 ，1 男 ，2 女')
    avatar_url = models.CharField(max_length=255,null=True, verbose_name='头像')
    phone =models.CharField(max_length=255, null=True,verbose_name='手机号')
    create_time = models.DateTimeField(null=False, auto_now=True, verbose_name='创建时间')
    last_login_time = models.DateTimeField(null=True, verbose_name='最后登录时间')
    email = models.CharField(max_length=255,null=True, verbose_name='邮箱')
    is_delete = models.SmallIntegerField(choices=DELETE_CHOICES, default=0, verbose_name='0 正常 1 删除')
    is_enable = models.SmallIntegerField( choices=ENABLE_CHOICES, default=0, verbose_name='0 启用 1 停用')
    remark = models.CharField(max_length=255, null=True, verbose_name='备注')
    user_id =models.SmallIntegerField(null=True, verbose_name='创建用户')
    is_login = models.SmallIntegerField(default=0, verbose_name='0 未登录， 1 已登录')
    user_no = models.CharField(null=True, max_length=255, verbose_name='账号')
    is_admin =models.SmallIntegerField( default="0")

    class Meta:
        db_table = 'ss_user'
        verbose_name  = '用户'
