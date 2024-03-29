"""
URL configuration for web_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from hello.views import hello_world
from django.views.static import serve

from web_django import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    # 1、固定的URL类型，字符串 /hello
    # 2、指定参数类型  /article/<int>
    # 3、使用正则表达式
    # 涵义：匹配到 hello 这个 url 的时候，放在 hello_world 函数里面进行处理
    # path('hello/', hello_world, name='hello_world')
    path('hello/', include('hello.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        path('__debug__/', include(debug_toolbar.urls))
    ]
