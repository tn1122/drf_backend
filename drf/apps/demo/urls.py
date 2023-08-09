from django.urls import path

from . import views

app_name = 'demo' #
#
# urlpatterns = [
# #     # path('demo', demo1),
#     path('demo', views.DemoView.as_view(), name='demo',)
# ]


# viewset
urlpatterns = [

    path('demo', views.DemoView.as_view(actions={'get': 'list'}),),
    path('demo/<int:pk>/', views.DemoView.as_view(actions={'get': 'retrieve'}))

]