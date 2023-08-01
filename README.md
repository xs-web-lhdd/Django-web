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

# 数据库
## 基础知识：
### 与 Flask 的区别
- Django 自带 ORM
- Flask 需要使用扩展（SQLAlchemy 只是其中一个）

### Django ORM 配置
- 项目配置(settings.py)
- 安装依赖
#### 配置选项
- default —— 默认的数据库，可配置多个数据，使用名称来区分
- ENGINE —— 数据库引擎
```python
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle'
```
- NAME —— 数据库名称
- USER —— 数据库登陆用户名
- PASSWORD —— 数据库登陆密码
- HOST —— 数据库访问地址
- PORT —— 数据库访问端口

- sqlite3 的配置选项：只需要指定数据库引擎和数据库文件名称即可

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_django',
        'USER': 'root',
        'PASSWORD': '1234567890',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```

#### 安装依赖
`pip install mysqlclient`

#### 数据库类型
##### 文本
- CharField、TextField 字符串、文本
- FileField、ImageField 文件、图片
- FilePathField 文件路径
- EmailField 邮件地址
- URLField URL地址
##### 数字（整数）
- IntegerField 整数
- SmallIntegerField 整数
- BigIntegerField 整数
- BooleanField 布尔值(1, 0)
- PositiveIntegerField 正整数
##### 日期与时间
- DateField 日期
- TimeField 时间
- DateTimeField 时期时间
##### 特殊类型
- OneToOneField 一对一关联
- Foreignkey 外键关联
- ManyToManyField 多对多关联
- GenericForeignKey 复合关联

### 模型同步 ！！！
- 先编写一个模型：
```python
from django.db import models

# Create your models here.
class User(models.Model):
    """用户模型"""
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '帅哥'),
        ('0', '美女')
    ), default='1')
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    remark = models.CharField('备注', max_length=64, null=True, blank=True)
    email = models.EmailField('用户的邮箱', max_length=64, null=True, blank=True)
    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)
```
- 前提：确认 settings.py
  - 已将模型添加到 INSTALLED_APPS
  - 确认数据库有没有手动创建，确认数据库配置是否正确
- 步骤一：检查模型是否编写正确
  - `python manage.py check`
- 步骤二：使用 makemigrations 生成同步原语
  - `python manage.py makemigrations`
- 步骤三：使用 migrate 执行同步
  - `python manage.py migrate`

<br/>掌握模型同步就再也不需要去数据库改字段了！

### 数据库的元数据
#### 元数据的描述
- 使用 Meta 类来表示
- 对模型的补充说明
- 示例：
```python
class Meta:
    verbose_name = '用户基础信息'
    verbose_name_plural = '用户基础信息'
    db_table = 'oauth_user'
```
#### 参数含义：
  - db_table 模型映射的数据库表的名称
  - ordering 指定数据表的模型排序规则
  - verbose_name 供编程查看的字段名称（便于阅读）
  - abstract 抽象类，抽象类不会生成数据库表（可以将公共内容抽取出来成一个类，然后让其他类继承此类）
  - proxy 代理模型（对父模型的功能进行扩充）

<br/>元数据设置可以是ORM的模型功能更加强大，使用元数据可以指定数据库表名称，表内公共字段抽取成公共类供其他类继承

### 外键关联类型
#### 一对一
- `OneToOneField(to, on_delete, parent_link=False, **options)`
- 举例：用户信息进行分表
#### 一对多
- `ForeignKey(to, on_delete, **options)`
- 举例：用户提问
#### 多对多
- `ManageToManage(to, **options)`
- 举例：收藏问题
#### 模型的参数选项
- to 关联的模型（必传）
  - 模型类
  - 模型类（字符串）
  - self
- on_delete 删除选项（必传）
  - CASCADE：关联删除
  - PROTECT：受保护，不允许被删除
  - SET_NULL：设置为None，需要添加选项null=True
  - SET_DEFAULT：设置为默认值，需要添加选项 default
  - SET()：传参设置值
  - DO_NOTHING：什么也不做
- related_name 是否需要反向引用，反向引用的名称
- related_query_name 反向引用的名称

### 复合类型 ！！！难点
#### 举例：这里有订单表和景点表，建立对应评论表：
```python
class Sight(models.Model):
    """景点表"""
    name = models.CharField('景点名称', max_length=64)
    address = models.CharField('景点地址', max_length=64)


class Order(models.Model):
    """订单表"""
    sn = models.CharField('订单号', max_length=64)
    amount = models.FloatField('订单金额')


class SightComment(models.Model):
    """景点评论"""
    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('分数', default=5)


class OrderComment(models.Model):
    """订单评论"""
    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('分数', default=5)
```

#### 字段解读
- ContentType 类容模型
- ForeignKey(ContentType) 关联复合模型
- GenericForeignKey 关联模型 
- GenericRelation 反向关联

<br/>更改后的示例：
```python
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Sight(models.Model):
    """景点表"""
    name = models.CharField('景点名称', max_length=64)
    address = models.CharField('景点地址', max_length=64)
    comments = GenericRelation('Comment', related_query_name='sight_comments')


class Order(models.Model):
    """订单表"""
    # order = Order()
    # comments = order.comments
    sn = models.CharField('订单号', max_length=64)
    amount = models.FloatField('订单金额')
    comments = GenericRelation('Comment', related_query_name='order_comments')


class Comment(models.Model):
    """所有评论"""
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('分数', default=5)
```

## CRUD
### 练习 CRUD 前构建的数据库的表
```python
from django.db import models


# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField('添加字段时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)

    class Meta:
        abstract = True


class User(CommonModel):
    """用户基本信息"""
    USER_STATUS = (
        (1, '正常'),
        (0, '删除')
    )
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=256)
    nickname = models.CharField('用户昵称', max_length=64, null=True, blank=True)
    avatar = models.ImageField('用户头像', upload_to='avatar', null=True, blank=True)
    status = models.SmallIntegerField('用户状态', default=1, choices=USER_STATUS)
    is_super = models.BooleanField('是否为超级用户', default=False)

    class Meta:
        db_table = 'demo_user'


class UserProfile(CommonModel):
    """用户详细信息"""
    SEX = (
        (1, '男性'),
        (0, '未知'),
        (2, '女性')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='关联用户')
    username = models.CharField('用户名', max_length=64, unique=True)
    real_name = models.CharField('真实姓名', max_length=64, null=True, blank=True)
    sex = models.SmallIntegerField('用户性别', default=0, choices=SEX)
    mamix = models.CharField('用户格言', max_length=128, null=True, blank=True)
    address = models.CharField('用户地址', max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'demo_user_profile'


class LoginHistory(models.Model):
    """用户的登陆历史"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history', verbose_name='关联的用户')
    username = models.CharField('用户名', max_length=64)
    login_type = models.CharField('登陆平台', max_length=64)
    ip = models.CharField('IP地址', max_length=32, default='')
    ua = models.CharField('登陆的来源', max_length=512, default='')
    created_at = models.DateTimeField('登陆时间', auto_now_add=True)

    class Meta:
        db_table = 'demo_user_history'
        # 用登陆时间进行排序，默认从小到大，添加 - ，变为从大到小
        ordering = ['-created_at']
```
### Django shell
- 从控制台(terminal)进入 `python manage.py shell`
- 打开 pycharm 的控制台即可

### 使用 ORM 新增数据
- 使用 save() 保存数据
- 使用 create() 新增数据
- 使用 bulk_create() 批量新增数据
#### 使用 save() 保存数据
- 示例代码：
```python
from demo.models import User

user_obj = User(username='admin',password='password')
user_obj.save()
```
#### 使用 create() 新增数据
- 示例代码：
```python
user_obj = User.objects.create(username='刘豪', password='password', nickname='张伟伟粉丝1号')
user_obj.pk # 返回新增用户的 id
```
#### 使用 bulk_create() 批量新增数据
- 示例代码：
```python
user1 = User(username='伟杰1',password='password'),
user2 = User.objects.create(username='伟杰2', password='password', nickname='我是伟杰我最帅')
user_list = [user1, user2]
User.objects.bulk_create(user_list)
```
#### 外键关联数据的插入
- 示例代码
```python
user = User(username='admin', password='password')
LoginHistory.objects.create(user=user, *args, **kwargs)
# 或者
LoginHistory.objects.create(user_id=user.id, username='admin',login_type='web登陆')
```

### 使用 ORM 实现简单查询
- get(**kwargs) 按照查询条件返回单挑数据
- latest(*fields) / earliest(*fields) 返回最晚/最早的一条记录
- first()/last() 返回第一条/最后一条数据
- 使用 all() 查询所有数据
#### 使用 get() 查询单条数据
```python
user_obj = User.objects.get(username='admin')
# 获取 id username
user_obj.id
```
#### latest(*fields) / earliest(*fields) 返回最晚/最早的一条记录
```python
# 最晚
latest = LoginHistory.objects.latest('created_at')
# 最早
latest = LoginHistory.objects.earliest('created_at')
```
#### 使用 all() 查询所有数据
- 实例代码
```python
User.objects.all()
```
#### 编程技巧
- 注意异常的处理
  - DoesNotExist 查询的记录不存在
  - MultipleObjectsReturned 查询的记录有多条
- 打印模型字符串 \_\_str__() 的使用
```python
# 在 User 表中加入以下函数
def __str__():
    return 'User: {}'.format(username)
```
#### Django 提供给的编程技巧
- 若有则返回，若无则创建后返回 `object, created = User.objects.get_or_create()`
- 如果没有则触发 404 异常 `get_object_or_404`

### 使用 ORM 实现数据修改
- 使用 save() 修改单条数据
- 使用 update() 批量修改数据
- 使用 bulk_update() 批量修改数据
#### 使用 save() 修改单条数据
```python
# 感觉这样修改数据很方便
user_obj = User.objects.get(username='admin')
user_obj.nickname = '管理员'
user_obj.save()
```
#### 使用 update() 批量修改数据
```python
user_list = User.objects.all()
user_list.update(status=0)
```
<br/>条件：注意不能修改外键关联的对象
#### 使用 bulk_update() 批量修改数据
方法使用：bulk_update(objs, fields, batch_size=None)
- objs 需要修改的记录列表
- fields 指定需要修改的字段
- batch_size 每次提交多少条记录进行修改

### 使用 ORM 实现数据的物理删除
- 使用模型的 delete() 删除数据
  - 删除单条数据
```python
  user_obj = User.objects.get(username='刘豪')
  user_obj.delete()
```
  - 删除多条数据（批量删除）
```python
  User.objects.all().delete()
```
<br/>物理删除：将数据从数据库干掉、干掉了就不占磁盘空间了、干掉了就找不回来了
<br/>逻辑删除：将数据标记删除、删除后还占磁盘空间、删除后还可以恢复、删除后通过查询条件不展示给用户

### 结果集合 QuerySet
- QuerySet 表示从数据库中取出来的对象的集合
- 它可以有零个、一个或者多个过滤器(filter)
- 从模型的Manager那里取得QuerySet
- QuerySet的筛选结果本身还是QuerySet
- QuerySet是惰性的
```python
user_list = User.objects.all()
user_obj = User.objects.get(pk=3)
user_list.filter(status=1)
# 拿到数据数量
user_list.count()
# 判断数据是否存在
user_list.exists()
# 链式查询方法
# all() # 查询所有记录
# none() # 创建一个空的结果集
# using() # 使用指定的数据库查询（多数据库支持）
# filter() # 筛选出满足条件的多条记录
User.objects.all().filter(is_super=1).count()
# exclude() # 排除满足条件的多条记录
User.objects.all().exclude(is_super=1).count()
# order_by() # 对查询的记录排序
User.objects.all().order_by('-id')
```
#### 自定义模型管理器
```python
class User(models.Model):
    # ...
    users = models.Manager()
```
<br/>然后可以通过 `User.users.all()` 进行查询

#### 获取数据库语句
```python
user_list = User.users.all()
print(user_list.query)
# SELECT `demo_user`.`id`, `demo_user`.`created_at`, `demo_user`.`updated_at`, `demo_user`.`username`, `demo_user`.`password`, `demo_user`.`nickname`, `demo_user`.`avatar`, `demo_user`.`status`, `demo_user`.`is_super` FROM `demo_user`
```

### 查询条件
- 相等/等于/布尔条件
- 是否包含 ** 字符串
- 以 ** 开始/结束
- 日期及时间
- 外键关联

#### 相等/等于
- exact 等于 ** 中（默认的形式），如：`id_exact=6` 或者 `id=6`
- iexact 像 ** 值，如：`name_iexact='zhangsan'`
```python
user_list = User.objects.all().filter(id=6)
user_list = User.objects.all().filter(id__exact=6)
user_list = User.objects.all().filter(username__exact='admin')
user_list = User.objects.all().filter(username__iexact='伟杰')
```
#### 布尔条件
- gt 大于某个值
- gte 大于或等于某个值
- lt 小于某个值
- lte 小于或等于某个值
- isnull 是否为空值
```python
User.objects.all().filter(status__gt=0)
User.objects.all().filter(avatar__isnull=True)
```
#### 是否包含 ** 字符串
- contains 包含 ** 值，如：`name_contains='san'`
- icontains 包含 ** 值，不区分大小写，如：`name_contains='san'` # ZhangSan zhangsan 都满足条件
- 在 ** 选项（列表）之内：`in`
```python
User.objects.filter(username__contains='伟杰')
User.objects.filter(username__in=['admin', '伟杰7'])
```
#### 以 ** 开始/结束
- 以 ** 开始 ``startswith`` 、`istartswith`
- 以 ** 结束 ``endswith``、``iendswith``
```python
User.objects.filter(username__startswith='伟杰')
```
#### 日期及时间
- date 日期
- year 年
- month 月份
- day 天
- hour/minute/second 时分秒
- week/week_day 星期
```python
from datetime import datetime
d = datetime(2025, 5, 11).date()
User.objects.filter(created_at__date=d)
```
#### 外键关联
- 查询在线问答系统中某个用户的回答 ``filter(user__username='admin')``
```python
# 去 profile 关联的 user 中查出用户名是 admin 的 profile 数据
UserProfile.objects.filter(user__username='admin')
# 去 profile 关联的 user 中查出用户名包含 伟杰 的 profile 数据
UserProfile.objects.filter(user__username__contains='伟杰')
```

### 按多个条件查询
#### filter 的深入使用
```python
# 示例：有效的管理员
User.objects.filter(nickname__icontains='管理员').filter(status=1)
# 或者
User.objects.filter(nickname__icontains='管理员', status=1)
```
#### & 运算符
```python
User.objects.filter(nickname__icontains='管理员')&User.objects.filter(status=1)
```
#### Q() 函数
- 使用 Q() 函数实现复杂的查询
- Q() 函数支持 &(且)  和  |(或)，对应 SQL 中的 AND 和 OR
```python
from django.db.models import Q
query1 = Q(nickname__icontains='管理员', status=1)
User.objects.filter(query1)
# 或者
query2 = Q(nickname__icontains='管理员') & Q(status=1)
User.objects.filter(query2)
```

### 查询优化
#### 安装 Django-debug-toolbar
去官网：`https://pypi.org/` 找 `Django-debug-toolbar` ，按照教程进行配置 `https://pypi.org/project/django-debug-toolbar/`

#### 优化外键关联查询
- QuerySet.select_related() 将外键关联的对象查询合并到主查询，一次性查询结果，减少 SQL 执行的数量
#### 使用 SQL 查询
- 方式一：使用管理器的 raw(sql) 函数
```python
raw(raw_query, params=None, translations=None)
# 返回 django.db.models.query.RawQuerySet 实例
```
- 方式二：获取数据库连接、游标、直接执行sql
  - 获取数据库连接 ``from django.db import connection``
  - 从连接得到游标 ``cursor = connection.cursor()``
  - 执行SQL ``cursor.execute('SELECT * FROM table WHERE baz=%s', [baz])``
  - 查询结果 ``row = cursor.fetchone()``

### 分页处理
- 对查询结果集QuerySet进行分片
- 使用 django.core.paginator 进行分页处理
- 使用 ListView 进行分页
#### 对查询结果集QuerySet进行分片
- 返回前 n 个对象 `User.objects.all()[:10]`
- 返回第 11 到第 20 个对象 ``User.objects.all()[10:20]``
#### 使用 django.core.paginator 进行分页处理
- 步骤一：取得分页器 `Paginator(objects, page_size)`
  - objects: 要进行分页的数据
  - page_size: 每页的数据多少
- 步骤二：取得页面实例 `page=p.get_page(page_num)`
  - page_num: 当前页的页码，如第几页
<br/>示例代码：
```python
user_list = User.objects.all()
p = Paginator(user_list, 15)
# get_page 可以处理异常输入，page 不能处理异常输入
page_data = p.get_page(3)
page_data = p.page(3)
```
#### 使用 ListView 进行分页
- page_obj 分页数据，如页码，当前第几页
- object_list 当前页的数据列表

### 聚合与统计
#### 内置聚合函数
- sum 求和
- avg 求平均
- count 计数
- max/min 最大值/最小值
##### 实现数据统计
- 使用 aggregate 从整个查询结果集生成统计数据
```python
from django.db.models import Avg
Grade.objects.all().aggregate(Avg('score'))
```
##### 实现聚合查询
- 使用 annotate 为查询结果集中的每一项生成统计数据
```python
from django.db.models import Sum
q = Student.objects.annotate(Sum('stu_grade_score'))
```

### 数据的一致性 ！！！
F() 函数的使用
- F() 函数从数据库操作层面修改数据
- F() 函数可避免同时操作时竞态条件


