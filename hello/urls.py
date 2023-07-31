from django.urls import path, re_path
from hello.views import hello_world, hello_china, article_list, search, http_request, http_response

urlpatterns = [
    path('world/', hello_world, name='hello_world'),
    path('china/', hello_china, name='hello_china'),
    # path('article/<int:month>/', article_list, name='hello_month'),
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list, name='hello_month'),
    path('search/', search, name='search'),
    path('request/', http_request, name='http_request'),
    path('response/', http_response, name='http_response'),
]
