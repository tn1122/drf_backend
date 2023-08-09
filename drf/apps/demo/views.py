from django.shortcuts import render


# Create your views here.

#### 视图继承关系####

# 1 视图函数
#
# def demo1(request, *args, **kwargs ):
#     #视图函数
#
#     return HttpResponse('函数视图')
# from django.http import HttpResponse


# ------------------------------------------
# # 2 类视图
# from  django.views import View
# from django.views.generic import View
#
# class DemoView(View):
#
#     def get(self, request):
#
#         return HttpResponse('类视图')
#

# ------------------------------------------
# drf

# 基类一 Apiview
# from rest_framework.views import APIView
# from rest_framework.response import Response
# class DemoView(APIView):
#
#     """
#     关系： APIView 继承 View
#     1 APIView 重写 了dispatch，封装了request请求
#     2 传入到视图方法中的是REST framework的Request对象，而不是Django的HttpRequeset对象
#     3身份认证、权限检查、流量控制
#     4 添加了异常捕获，只是追Apiview 源码可以忽略这一点
#     5 响应 Response，  视图会为响应数据设置（render）符合前端要求的格式 只是追Apiview 源码可以忽略这一点
#     支持定义的属性：
#        authentication_classes 列表或元祖，身份认证类
#        permissoin_classes 列表或元祖，权限检查类
#        throttle_classes 列表或元祖，流量控制类
#     """
#     def get(self, request):
#         return Response('Apiview类视图')
# ------------------------------------------

# 基类二 GenericAPIView

# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
#
# class DemoView(GenericAPIView):
#     """
#     关系： GenericAPIView继承 APIView
#      APIView 没有重写 dispatch，理解APiview即可
#      主要变化，主要是序列化和queryset
#      追源码不难看出一下几点
#          serializer_class 指明视图使用的序列化器
#          queryset 指明使用的数据查询集,
#          pagination_class 指明分页控制类
#          filter_backends 指明过滤控制后端
#     """
#     def get(self, request):
#         return Response('GenericAPIView')

# ------------------------------------------

# 拓展类

# from rest_framework.mixins import ListModelMixin
# from rest_framework.generics import GenericAPIView
# class DemoView(ListModelMixin, GenericAPIView):
#     queryset =
#     def get(self, request):
#         return self.list(request)

# ------------------------------------------

# from rest_framework.mixins import CreateModelMixin
#
# from rest_framework.response import Response
# from .serializer import SsuerSerializer


# class DemoView(CreateModelMixin, GenericAPIView):
#     # 模拟 request 的参数
#
#     serializer_class = SsuerSerializer
#     def get(self, request):
#
#         return Response('get请求')
#
#     def post(self, request, *args, **kwargs):
#         # 参数
#         #{"user_name": "wang", "password": "123456","user_id":1 }
#         # 反序列化 传参
#         print(request.data)
#         serializer = SsuerSerializer(data=request.data)
#         resp = serializer.is_valid()
#         if not resp:
#             return Response({"error":serializer.errors, 'code':400})
#         return self.create(request)


# ------------------------------------------

# from rest_framework.generics import GenericAPIView, CreateAPIView
#
# from demo.serializer import SsuerSerializer
#
#
# class DemoView(CreateAPIView):
#     # 把create 方法提交
#     serializer_class = SsuerSerializer


# ------------------------------------------

# 视图集
# from rest_framework.viewsets import ViewSet
# from .models import SsUser
# from .serializer import SsuerSerializer
# from rest_framework.response import Response
#
# class DemoView(ViewSet):
#     '''
#     源码中实现方式是通过as_view 对方法进行动态 设置， 也就是说不是单一的命名 get, post 等方法，可以自定义方法名称进行url 映射
#          for method, action in actions.items():
#                 handler = getattr(self, action)
#                 setattr(self, method, handler)
#
#
#     视图集ViewSe,字面理解将所有方法放到一个视图下，
#     主要是为了兼容 get 查询单个数据和多个数据的情况（因为一个视图下不能写两个get方法）
#     list() 提供一组数据
#     retrieve() 提供单个数据
#     create() 创建数据
#     update() 保存数据
#     destory() 删除数据
#     '''
#
#     def list(self, request):
#         ss_users = SsUser.objects.all()
#         data = SsuerSerializer(ss_users, many=True)
#         return Response(data.data)
#
#     def retrieve(self, request, pk):
#         # ss_user = SsUser.objects.get(id=pk)
#         ss_user = SsUser.objects.filter(id=pk).first()
#         if not ss_user:
#             return Response('查询失败')
#         data = SsuerSerializer(ss_user)
#         return Response(data.data)

# ------------------------------------------

# GenericViewSet

# from rest_framework.viewsets import GenericViewSet
# from .serializer import SsuerSerializer
# from .models import SsUser
# from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
# class DemoView( ListModelMixin,RetrieveModelMixin,GenericViewSet):
#
#     '''
#     继承自GenericAPIView与ViewSetMixin
#     实现了调用as_view()时传入字典（如{'get':'list'}）
#     的映射处理工作的同时，还提供了GenericAPIView提供的基础方法，可以直接搭配Mixin扩展类使用
#     '''
#
#     serializer_class = SsuerSerializer
#     queryset = SsUser.objects.all()
# ------------------------------------------


# ModelViewSet
# from rest_framework.viewsets import ModelViewSet
# from .serializer import SsuerSerializer
# from .models import SsUser
#
# class DemoView(ModelViewSet):
#
#     '''
#     继承自GenericViewSet，
#     包括了ListModelMixin、RetrieveModelMixin、CreateModelMixin、
#     UpdateModelMixin、DestoryModelMixin。
#     '''
#
#     serializer_class = SsuerSerializer
#     queryset = SsUser.objects.all()


# ------------------------------------------
