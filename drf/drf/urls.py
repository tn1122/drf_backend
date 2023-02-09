"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path
from apps.allapp import URLS_APPS
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views import static

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

urlpatterns = [re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static')]
urlpatterns += staticfiles_urlpatterns()

for app, app_urls in URLS_APPS.items():
    # 开始自动装载各app.urls

    app_urlresolver = getattr(app_urls, 'urlpatterns', [])

    app_urlpattern = re_path(f'api/v1/{app}/', (app_urlresolver, app, app))

    urlpatterns.append(app_urlpattern)