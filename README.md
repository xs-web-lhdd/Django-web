# Django

## Django项目结构
- web_django    # 项目目录
  - __init__.py   # 包的入口文件
  - settings.py   # 项目配置文件
  - urls.py       # url访问地址配置文件
  - wsgi.py       # 部署配置
  - asgi.py       # 部署配置
- manage.py     # 命令行管理工具

## 启动项目：
- 命令行指令：``python manage.py runserver``
- 指定端口：``python manage.py runserver 8080``
- pycharm 配置启动：
  - 脚本路径：`C:\Users\LiuHao\Desktop\web_django\manage.py`
  - 形参：`runserver 8080`

## 创建模块：
- 创建hello模块：`python manage.py startapp hello`

## 路由：
### path() 参数解释：
- route: URL 匹配规则
- view: 视图函数
- name: 路由的名称
- **kwargs: 其他参数

### include() 参数解释：
- urls: URL 匹配规则列表
- namespace: 命名空间

### 获取 URL 参数;
- 获取 RUL 中的指定类型的参数
```python
# URL 规则：
path('article/<int:month>/', article_list, name='hello_month')
# 视图函数：
def article_list(request, month):
    """
    :param month: 今年某一个月的文章列表
    """
    return HttpResponse('article {}'.format(month))
# 输入 URL：
http://127.0.0.1:8080/hello/article/100/
```
- 获取 URL 中的正则匹配的参数：
```python
# URL 规则：
re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list, name='hello_month'),
# 视图函数：
def article_list(request, month):
    """
    :param month: 今年某一个月的文章列表
    """
    return HttpResponse('article {}'.format(month))
# 输入 URL：
http://127.0.0.1:8080/hello/article/10/ #可以访问
http://127.0.0.1:8080/hello/article/100/ #不在 1-12 之间，不可以访问
```

### 获取 GET 参数
- 获取请求中（GET / POST等）参数
```python
# URL 规则：
path('search/', search, name='search')
# 输入URL
http://127.0.0.1:8080/hello/search/?name=五月天
# 视图编写
def search(request):
    """GET参数的获取"""
    name = request.GET.get('name', '')
    print('name --------->>>>>>>>>>>>>', name)
    return HttpResponse('查询成功！')
```

### 请求对象
```python
def http_request(request):
    """请求练习"""
    # 1、请求方式
    print('请求方式 ----------->>>>>>>>>', request.method)
    # 2、请求头信息
    headers = request.META
    print('请求头信息 ----------->>>>>>>>>', headers)
    # 获取 user-agent
    ua = request.META.get('HTTP_USER_AGENT', None)
    print('user-agent -------->>>>>>>>>', ua)
    print('user-agent -------->>>>>>>>>', request.headers['User-Agent'])
    print('user-agent -------->>>>>>>>>', request.headers['user-agent'])
    # 3、获取请求参数
    name = request.GET.get('name', '没有传递参数的默认值')
    print('获取请求参数 ----------->>>>>>>>>', name)
    return HttpResponse('响应！')
```

### 响应对象
- HttpResponse
- HttpResponseRedirect  重定向
- JsonResponse  响应json
- FileResponse  响应文件

#### HttpResponse
- status 设置 HTTP 响应状态码
- status_code 查看 HTTP 响应状态码
- content_type 设置响应的类型
- write() 写入响应内容
```python
def http_response(request):
    """响应练习"""
    resp = HttpResponse('响应内容', status=201)
    resp.status_code = 200
    print('resp.status_code ----->>>>>', resp.status_code)
    return resp
```

#### JsonResponse
```python
def http_response(request):
    """响应练习"""
    user_info = {
        'name': '张三',
        'age': 34
    }
    return JsonResponse(user_info)
```

#### FileResponse
```python
response = FileResponse(open('myfile.png', 'rb'))
```

#### 重定向
- 使用 HttpResponseRedirect 重定向
- 使用 redirect() 快捷方式

## static.serve 处理静态文件
- 在项目 settings.py 中添加配置
```python
import os.path

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'medias') 
```
- 在项目 urls.py 中添加配置
```python
from django.views.static import serve
urlpatterns += [
  re_path(r'^media/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIA_ROOT,
  })
]
```

